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
df_high_severity = df[df["High_Severity"] > 0].copy()

if df_high_severity.empty:
    print("No high-severity vulnerabilities detected in the analyzed commits.")
else:
    # Function to get commit date using Git
    def get_commit_date(commit_hash):
        result = subprocess.run(
            ["git", "show", "-s", "--format=%ci", commit_hash],  # Fetch commit date
            cwd=repo_path, text=True, capture_output=True
        )
        return result.stdout.strip()

    # Get commit dates
    df_high_severity["Commit_Date"] = df_high_severity["Commit"].apply(get_commit_date)
    df["Commit_Date"] = df["Commit"].apply(get_commit_date)

    # Convert to datetime format
    df["Commit_Date"] = pd.to_datetime(df["Commit_Date"], utc=True)
    df_high_severity["Commit_Date"] = pd.to_datetime(df_high_severity["Commit_Date"], utc=True)
    df = df.sort_values(by="Commit_Date")

    # Initialize columns for fix commits
    df_high_severity["Fixed_In_Commit"] = None
    df_high_severity["Fix_Date"] = None
    df_high_severity["Duration_Days"] = None  # For duration calculation
    df_high_severity["Commits_Between"] = None  # For commit count calculation

    for index, row in df_high_severity.iterrows():
        commit_date = pd.to_datetime(row["Commit_Date"], utc=True)  # Convert to Timestamp
        commit_hash = row["Commit"]

        # Find the next commit where high severity is 0 (vulnerability is fixed)
        fixed_commit = df[(df["Commit_Date"] > commit_date) & (df["High_Severity"] == 0)]

        if not fixed_commit.empty:
            fix_commit_row = fixed_commit.iloc[0]  # First commit where issue is resolved
            df_high_severity.at[index, "Fixed_In_Commit"] = fix_commit_row["Commit"]
            df_high_severity.at[index, "Fix_Date"] = fix_commit_row["Commit_Date"]

            # Calculate the duration between detection and resolution
            df_high_severity.at[index, "Duration_Days"] = (fix_commit_row["Commit_Date"] - commit_date).days

            commit_count = subprocess.run(
                ["git", "rev-list", "--count", f"{commit_hash}..{fix_commit_row['Commit']}"],
                cwd=repo_path, text=True, capture_output=True
            )
            df_high_severity.at[index, "Commits_Between"] = int(commit_count.stdout.strip())

    # Keep only required columns
    df_high_severity = df_high_severity[
        ["Commit", "High_Severity", "Commit_Date", "Fixed_In_Commit", "Fix_Date", "Duration_Days", "Commits_Between"]
    ]

    output_csv = os.path.join(repo_path, "high_severity_timeline.csv")
    df_high_severity.to_csv(output_csv, index=False)

    print(f"📊 High Severity timeline saved to: {output_csv}")

    # Plot the timeline of high-severity vulnerabilities with lines connecting introduction to fix
    plt.figure(figsize=(12, 6))
    
    # Plot introduction points
    plt.scatter(df_high_severity["Commit_Date"], df_high_severity["High_Severity"], 
                color="red", marker="o", label="High Severity Introduced", s=100)

    # Plot fix points
    plt.scatter(df_high_severity["Fix_Date"], df_high_severity["High_Severity"], 
                color="green", marker="x", label="Fixed", s=100)

    # Draw lines connecting introduction to fix
    for _, row in df_high_severity.iterrows():
        if pd.notna(row["Fix_Date"]):  # Ensure a fix exists
            plt.plot([row["Commit_Date"], row["Fix_Date"]], 
                     [row["High_Severity"], row["High_Severity"]], 
                     linestyle="--", color="gray")

    plt.xlabel("Date")
    plt.ylabel("High Severity Count")
    plt.title("Timeline of High-Severity Vulnerabilities and Fixes")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)

    # Save plot explicitly
    plot_path = os.path.join(repo_path, "high_severity_timeline.png")
    plt.savefig(plot_path, bbox_inches="tight", dpi=300)
    plt.close()

    print(f"📊 Plot saved to: {plot_path}")

