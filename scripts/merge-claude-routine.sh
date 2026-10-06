#!/usr/bin/env bash
# Merge only this push's head; newer pushes are handled by their own workflow run.
set -euo pipefail

if [[ $# -ne 3 || ! "$1" =~ ^[1-9][0-9]*$ || ! "$2" =~ ^[0-9a-f]{40}$ ]]; then
  echo "usage: bash scripts/merge-claude-routine.sh PR_NUMBER EXPECTED_SHA BRANCH" >&2
  exit 1
fi

number="$1"
expected_sha="$2"
branch="$3"
max_attempts=12

delete_merged_branch() {
  # Unlike --delete-branch, this cannot delete commits pushed after the merge.
  local output ref status current_sha current_ref
  if output="$(git push --force-with-lease="refs/heads/$branch:$expected_sha" \
    origin ":refs/heads/$branch" 2>&1)"; then
    printf '%s\n' "$output"
    return
  fi
  printf '%s\n' "$output" >&2

  if ref="$(git ls-remote --exit-code origin "refs/heads/$branch")"; then
    read -r current_sha current_ref <<< "$ref"
    if [[ ! "$current_sha" =~ ^[0-9a-f]{40}$ || "$current_ref" != "refs/heads/$branch" ]]; then
      echo "Invalid remote branch response for $branch." >&2
      return 1
    fi
    if [[ "$current_sha" != "$expected_sha" ]]; then
      echo "Keeping $branch: a newer push arrived after the merge ($current_sha)."
      return
    fi
  else
    status=$?
    if [[ "$status" -eq 2 ]]; then
      echo "$branch was already deleted."
      return
    fi
    return "$status"
  fi
  echo "Merged PR #$number, but could not delete $branch." >&2
  return 1
}

read_pr() {
  local ref status current_sha current_ref
  pr_head_current=true
  snapshot="$(gh pr view "$number" \
    --json state,headRefOid,headRefName,mergeable,mergeStateStatus \
    --jq '[.state, .headRefOid, .headRefName, .mergeable, .mergeStateStatus] | @tsv')"
  IFS=$'\t' read -r state head_sha head_branch mergeable merge_state <<< "$snapshot"

  if [[ ! "$head_sha" =~ ^[0-9a-f]{40}$ ]]; then
    echo "Invalid PR #$number status response." >&2
    exit 1
  fi
  if [[ ! "$state" =~ ^(OPEN|MERGED)$ || "$head_branch" != "$branch" ]]; then
    echo "Cannot merge PR #$number: state=$state, branch=$head_branch." >&2
    exit 1
  fi
  if [[ "$head_sha" != "$expected_sha" ]]; then
    # GitHub's PR metadata can lag a just-pushed branch. The live ref decides
    # whether this event is superseded or still waiting for that metadata.
    if ref="$(git ls-remote --exit-code origin "refs/heads/$branch")"; then
      read -r current_sha current_ref <<< "$ref"
      if [[ ! "$current_sha" =~ ^[0-9a-f]{40}$ || "$current_ref" != "refs/heads/$branch" ]]; then
        echo "Invalid remote branch response for $branch." >&2
        exit 1
      fi
      if [[ "$current_sha" == "$expected_sha" ]]; then
        pr_head_current=false
        return
      fi
      echo "Skipping superseded push $expected_sha ($branch is now $current_sha)."
    else
      status=$?
      if [[ "$status" -ne 2 ]]; then
        exit "$status"
      fi
      echo "Skipping $branch: the branch was already deleted."
    fi
    exit 0
  fi
  if [[ "$state" == MERGED ]]; then
    echo "PR #$number is already merged."
    exit 0
  fi
}

for ((attempt = 1; attempt <= max_attempts; attempt++)); do
  read_pr
  if [[ "$pr_head_current" == false ]]; then
    echo "Waiting for PR #$number head metadata (attempt $attempt/$max_attempts)."
  elif [[ "$mergeable" == CONFLICTING || "$merge_state" == DIRTY ]]; then
    echo "Cannot merge PR #$number: merge conflicts." >&2
    exit 1
  elif [[ "$merge_state" =~ ^(BLOCKED|BEHIND|DRAFT)$ ]]; then
    echo "Cannot merge PR #$number: mergeStateStatus=$merge_state." >&2
    exit 1
  elif [[ "$mergeable" == UNKNOWN || "$merge_state" == UNKNOWN ]]; then
    echo "Waiting for GitHub to compute mergeability (attempt $attempt/$max_attempts)."
  elif [[ "$mergeable" == MERGEABLE && "$merge_state" =~ ^(CLEAN|HAS_HOOKS|UNSTABLE)$ ]]; then
    if output="$(gh pr merge "$number" --squash --match-head-commit "$expected_sha" 2>&1)"; then
      printf '%s\n' "$output"
      merged_state="$(gh pr view "$number" --json state --jq .state)"
      if [[ "$merged_state" != MERGED ]]; then
        echo "PR #$number is $merged_state; merge was not confirmed. Keeping $branch." >&2
        exit 1
      fi
      delete_merged_branch
      exit 0
    fi
    printf '%s\n' "$output" >&2
    # A concurrent push can also produce a head-commit lease mismatch. Re-read
    # before classifying the error so stale events exit without merging it.
    read_pr
    # This observed race is transient; authentication and policy errors are not.
    if [[ "$output" != *"Head branch is out of date"* ]]; then
      exit 1
    fi
  else
    echo "Cannot merge PR #$number: mergeable=$mergeable, mergeStateStatus=$merge_state." >&2
    exit 1
  fi

  if [[ "$attempt" -lt "$max_attempts" ]]; then
    sleep 5
  fi
done

echo "PR #$number did not become mergeable after $max_attempts attempts." >&2
exit 1
