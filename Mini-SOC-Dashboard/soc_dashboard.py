print("================================")
print("        MINI SOC DASHBOARD")
print("================================")

info_count = 0
warning_count = 0
error_count = 0
alerts = []

with open("security_logs.txt", "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
            alerts.append(line.strip())
        elif "ERROR" in line:
            error_count += 1
            alerts.append(line.strip())

print("\nSecurity Dashboard")
print("------------------")
print("INFO Logs:", info_count)
print("WARNING Logs:", warning_count)
print("ERROR Logs:", error_count)

print("\nSecurity Alerts")
print("---------------")

for alert in alerts:
    print(alert)

with open("soc_report.txt", "w") as report:
    report.write("MINI SOC DASHBOARD REPORT\n")
    report.write("=========================\n")
    report.write(f"INFO Logs: {info_count}\n")
    report.write(f"WARNING Logs: {warning_count}\n")
    report.write(f"ERROR Logs: {error_count}\n\n")
    report.write("Security Alerts:\n")

    for alert in alerts:
        report.write(alert + "\n")

print("\nReport saved as soc_report.txt")