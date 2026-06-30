import pandas as pd

print("================================")
print(" ENTERPRISE OFFICE NETWORK SOC")
print("================================")

employees = pd.read_csv("employees.csv")
devices = pd.read_csv("devices.csv")
logs = pd.read_csv("network_logs.csv")

risk_score = 0
alerts = []

for _, row in logs.iterrows():
    event = row["event"]

    if event == "Failed Login":
        risk_score += 2
        alerts.append(f"Failed Login detected from Employee ID {row['employee_id']} at {row['ip_address']}")

    elif event == "Unknown Device Connected":
        risk_score += 4
        alerts.append(f"Unauthorized device detected at IP {row['ip_address']}")

    elif event == "Suspicious External IP":
        risk_score += 5
        alerts.append(f"Suspicious external IP communication detected: {row['ip_address']}")

    elif event == "Malware Alert":
        risk_score += 6
        alerts.append(f"Malware alert detected for Employee ID {row['employee_id']}")

print("\nOffice Network Summary")
print("----------------------")
print("Total Employees:", len(employees))
print("Total Devices:", len(devices))
print("Total Logs:", len(logs))

print("\nSecurity Alerts")
print("---------------")
for alert in alerts:
    print("-", alert)

print("\nRisk Score:", risk_score)

if risk_score >= 15:
    print("Threat Level: HIGH")
elif risk_score >= 8:
    print("Threat Level: MEDIUM")
else:
    print("Threat Level: LOW")

with open("incident_report.txt", "w") as report:
    report.write("ENTERPRISE OFFICE NETWORK INCIDENT REPORT\n")
    report.write("=========================================\n")
    report.write(f"Total Employees: {len(employees)}\n")
    report.write(f"Total Devices: {len(devices)}\n")
    report.write(f"Total Logs: {len(logs)}\n")
    report.write(f"Risk Score: {risk_score}\n\n")
    report.write("Security Alerts:\n")

    for alert in alerts:
        report.write("- " + alert + "\n")

print("\nIncident report saved as incident_report.txt")