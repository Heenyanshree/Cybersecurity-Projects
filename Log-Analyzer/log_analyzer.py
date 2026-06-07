print("================================")
print("          LOG ANALYZER")
print("================================")

info_count = 0
error_count = 0
warning_count = 0

with open("sample_log.txt", "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1
        elif "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1

print("\nLog Analysis Report")
print("-------------------")
print("INFO Count:", info_count)
print("ERROR Count:", error_count)
print("WARNING Count:", warning_count)