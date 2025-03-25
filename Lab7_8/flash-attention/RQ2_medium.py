import pandas as pd
import os
import subprocess
import matplotlib.pyplot as plt

# Define repository path
repo_path = "/home/nidhi/Lab7_8/flash-attention"
csv_file = os.path.join(repo_path, "bandit_result.csv")

# Read the dataset
df = pd.read_csv(csv_file)

# Rename columns for consistency
df.columns = df.columns.str.replace(" ", "_")
df_medium_severity = df[df["Medium_Severity"] > 0].copy()

if df_medium_severity.empty:
    print("No medium-severity vulnerabilities detected in the analyzed commits.")
else:
    # Function to get commit date using Git
    def get_commit_date(commit_hash):
        result = subprocess.run(
            ["git", "show", "-s", "--format=%ci", commit_hash],  # Fetch commit date
            cwd=repo_path, text=True, capture_output=True
        )
        return result.stdout.strip()

    # Get commit dates
    df_medium_severity["Commit_Date"] = df_medium_severity["Commit"].apply(get_commit_date)
    df["Commit_Date"] = df["Commit"].apply(get_commit_date)

    # Convert to datetime format
    df["Commit_Date"] = pd.to_datetime(df["Commit_Date"], utc=True)
    df_medium_severity["Commit_Date"] = pd.to_datetime(df_medium_severity["Commit_Date"], utc=True)
    df = df.sort_values(by="Commit_Date")

    # Initialize columns for fix commits
    df_medium_severity["Fixed_In_Commit"] = None
    df_medium_severity["Fix_Date"] = None
    df_medium_severity["Duration_Days"] = None
    df_medium_severity["Commits_Between"] = None
    for index, row in df_medium_severity.iterrows():
        commit_date = pd.to_datetime(row["Commit_Date"], utc=True)  # Convert to Timestamp
        commit_hash = row["Commit"]

        # Find the next commit where medium severity is 0 (vulnerability is fixed)
        fixed_commit = df[(df["Commit_Date"] > commit_date) & (df["Medium_Severity"] == 0)]

        if not fixed_commit.empty:
            fix_commit_row = fixed_commit.iloc[0]  # First commit where issue is resolved
            df_medium_severity.at[index, "Fixed_In_Commit"] = fix_commit_row["Commit"]
            df_medium_severity.at[index, "Fix_Date"] = fix_commit_row["Commit_Date"]

            # Calculate the duration between detection and resolution
            df_medium_severity.at[index, "Duration_Days"] = (fix_commit_row["Commit_Date"] - commit_date).days

            commit_count = subprocess.run(
                ["git", "rev-list", "--count", f"{commit_hash}..{fix_commit_row['Commit']}"],
                cwd=repo_path, text=True, capture_output=True
            )
            df_medium_severity.at[index, "Commits_Between"] = int(commit_count.stdout.strip())

    # Keep only required columns
    df_medium_severity = df_medium_severity[
        ["Commit", "Medium_Severity", "Commit_Date", "Fixed_In_Commit", "Fix_Date", "Duration_Days", "Commits_Between"]
    ]

    output_csv = os.path.join(repo_path, "medium_severity_timeline.csv")
    df_medium_severity.to_csv(output_csv, index=False)

    print(f"📊 Medium Severity timeline saved to: {output_csv}")

    # Plot the timeline of medium-severity vulnerabilities with lines connecting introduction to fix
    plt.figure(figsize=(10, 5))

    # Plot introduction points
    plt.scatter(df_medium_severity["Commit_Date"], df_medium_severity["Medium_Severity"],
            color="orange", marker="o", label="Medium Severity Introduced", s=100)
    # Plot fix points
    plt.scatter(df_medium_severity["Fix_Date"], df_medium_severity["Medium_Severity"],
                color="green", marker="x", label="Fixed", s=100)

    # Draw lines connecting introduction to fix
    for _, row in df_medium_severity.iterrows():
        if pd.notna(row["Fix_Date"]):  # Ensure a fix exists
            plt.plot([row["Commit_Date"], row["Fix_Date"]],
                     [row["Medium_Severity"], row["Medium_Severity"]],
                     linestyle="--", color="gray")

    plt.xlabel("Date")
    plt.ylabel("Medium Severity Count")
    plt.title("Timeline of Medium-Severity Vulnerabilities and Fixes")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)

    # Save plot explicitly
    plot_path = os.path.join(repo_path, "medium_severity_timeline.png")
    plt.savefig(plot_path, bbox_inches="tight", dpi=300)
    plt.close()

    print(f"📊 Plot saved to: {plot_path}")

