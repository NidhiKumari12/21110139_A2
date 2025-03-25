import pandas as pd
import os
import matplotlib.pyplot as plt

# Define main folder path
main_folder = "/home/nidhi/Lab7_8"

# List of repositories
repos = ["flash-attention", "felt", "menray"]

# Initialize an empty DataFrame
df_cwe = pd.DataFrame()

# Loop through each repository
for repo in repos:
    csv_path = os.path.join(main_folder, repo, "bandit_result.csv")

    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=["CWEs"])  # Drop rows where CWEs is empty
        df["CWEs"] = df["CWEs"].astype(str).str.split(",")

        # Expand rows if multiple CWEs are in a single cell
        df = df.explode("CWEs")
        df["CWEs"] = df["CWEs"].str.strip()
        df["CWEs"] = pd.to_numeric(df["CWEs"], errors="coerce")  # Handle non-numeric CWEs

        cwe_counts = df["CWEs"].value_counts().reset_index()
        cwe_counts.columns = ["CWE", "Frequency"]

        df_cwe = pd.concat([df_cwe, cwe_counts])

df_cwe = df_cwe.groupby("CWE", as_index=False).sum()
df_cwe = df_cwe.sort_values(by="Frequency", ascending=False)
output_csv = os.path.join(main_folder, "CWE_Frequency.csv")
df_cwe.to_csv(output_csv, index=False)

print(f"\n✅ CWE frequency report saved to: {output_csv}")

top_cwes = df_cwe.head(5)

# Plot
plt.figure(figsize=(8, 5))
plt.bar(top_cwes["CWE"].astype(str), top_cwes["Frequency"], color=["red", "blue", "green", "orange", "purple"])

plt.xlabel("CWE ID")
plt.ylabel("Frequency")
plt.title("Top 5 Most Frequent CWEs in OSS Repositories")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis="y", linestyle="--", alpha=0.7)
plot_path = os.path.join(main_folder, "Top5_CWE_Frequency.png")
plt.savefig(plot_path, bbox_inches="tight", dpi=300)
plt.close()

print(f"\n✅ CWE Frequency plot saved to: {plot_path}")
