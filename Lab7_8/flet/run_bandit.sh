#!/bin/bash

mkdir -p bandit_reports  # Create a folder to store Bandit reports

# Get the last 200 non-merge commits
git log --no-merges --pretty=format:"%H" -n 200 > commits.txt

count=0  
while read commit; do
    if [[ $count -ge 100 ]]; then  # Stop after 100 valid commits
        break
    fi

    echo "Checking commit: $commit"

    # Get modified Python files in the commit (excluding myenv/)
    changed_files=$(git diff-tree --no-commit-id --name-only -r "$commit" | grep '\.py$' | grep -v 'flet_env/' )

    if [[ -n "$changed_files" ]]; then  # If Python files were modified
        echo "Python files modified in $commit:"
        echo "$changed_files"

        # Run Bandit on modified Python files (excluding myenv)
        bandit -r $(echo "$changed_files") -x flet_env -f json -o "bandit_reports/report_$commit.json"

        # Remove empty JSON reports
        if [[ ! -s "bandit_reports/report_$commit.json" ]]; then
            rm "bandit_reports/report_$commit.json"
            echo "No issues found in commit $commit, skipping report."
        else
            count=$((count + 1))  # Increment counter only if there's an issue
        fi
    else
        echo "Skipping commit $commit (No Python files changed)"
    fi

done < commits.txt

echo "✅ Analysis completed for $count commits with Python changes."
