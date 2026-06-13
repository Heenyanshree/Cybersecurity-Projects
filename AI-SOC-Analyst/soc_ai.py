print("================================")
print("      AI SOC ANALYST")
print("================================")

filename = input("Enter log file name: ")

with open(filename, "r") as file:
    logs = file.readlines()

info_count = 0
warning_count = 0
error_count = 0
alerts = []

for log in logs:
    if "INFO" in log:
        info_count += 1
    elif "WARNING" in log:
        warning_count += 1
        alerts.append(log.strip())
    elif "ERROR" in log:
        error_count += 1
        alerts.append(log.strip())

risk_score = warning_count + (error_count * 2)

print("\nSOC Analysis Report")
print("-------------------")
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)
print("Risk Score:", risk_score)

if risk_score >= 6:
    print("Threat Level: HIGH")
elif risk_score >= 3:
    print("Threat Level: MEDIUM")
else:
    print("Threat Level: LOW")

print("\nAI Alert Classification")
print("-----------------------")

for alert in alerts:
    alert_lower = alert.lower()

    if "sql injection" in alert_lower:
        threat_type = "Web Attack"
    elif "malware" in alert_lower:
        threat_type = "Malware"
    elif "failed login" in alert_lower or "brute force" in alert_lower:
        threat_type = "Authentication Threat"
    elif "suspicious network" in alert_lower:
        threat_type = "Network Threat"
    else:
        threat_type = "Unknown Threat"

    print(alert, "=>", threat_type)

with open("soc_ai_report.txt", "w") as report:
    report.write("AI SOC ANALYST REPORT\n")
    report.write("=====================\n")
    report.write(f"INFO: {info_count}\n")
    report.write(f"WARNING: {warning_count}\n")
    report.write(f"ERROR: {error_count}\n")
    report.write(f"Risk Score: {risk_score}\n\n")
    report.write("Alert Classification:\n")

    for alert in alerts:
        alert_lower = alert.lower()

        if "sql injection" in alert_lower:
            threat_type = "Web Attack"
        elif "malware" in alert_lower:
            threat_type = "Malware"
        elif "failed login" in alert_lower or "brute force" in alert_lower:
            threat_type = "Authentication Threat"
        elif "suspicious network" in alert_lower:
            threat_type = "Network Threat"
        else:
            threat_type = "Unknown Threat"

        report.write(f"{alert} => {threat_type}\n")

print("\nReport saved as soc_ai_report.txt")