import csv
import os
import json

# Folder where Bandit JSON reports are stored
REPORTS_FOLDER = "bandit_reports"
OUTPUT_CSV = "bandit_result.csv"

# CSV Headers
HEADERS = ["Commit", "High_Confidence", "Medium_Confidence", "Low_Confidence",
           "High_Severity", "Medium_Severity", "Low_Severity", "CWEs"]

# Open CSV file to write results
with open(OUTPUT_CSV, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(HEADERS)  # Write header row

    # Loop through all Bandit reports
    for report_file in sorted(os.listdir(REPORTS_FOLDER)):
        if report_file.endswith(".json"):
            commit = report_file.replace("report_", "").replace(".json", "")

            with open(os.path.join(REPORTS_FOLDER, report_file), "r") as file:
                data = json.load(file)

            high_conf, med_conf, low_conf = 0, 0, 0
            high_sev, med_sev, low_sev = 0, 0, 0
            cwes = set()

            for issue in data.get("results", []):
                confidence = issue.get("issue_confidence", "").upper()
                severity = issue.get("issue_severity", "").upper()
                cwe_data = issue.get("issue_cwe", {})

                # Count confidence levels
                if confidence == "HIGH":
                    high_conf += 1
                elif confidence == "MEDIUM":
                    med_conf += 1
                elif confidence == "LOW":
                    low_conf += 1

                # Count severity levels
                if severity == "HIGH":
                    high_sev += 1
                elif severity == "MEDIUM":
                    med_sev += 1
                elif severity == "LOW":
                    low_sev += 1

                # Extract CWE ID
                if isinstance(cwe_data, dict) and "id" in cwe_data:
                    cwes.add(str(cwe_data["id"]))

            # Write row to CSV
            writer.writerow([commit, high_conf, med_conf, low_conf,
                             high_sev, med_sev, low_sev, ", ".join(cwes)])

print(f"✅ Analysis completed! CSV saved as: {OUTPUT_CSV}")
