import subprocess

print("================================")
print("    FIREWALL RULE ANALYZER")
print("================================")

print("\nReading Windows Firewall Rules...\n")

try:
    result = subprocess.check_output(
        "netsh advfirewall firewall show rule name=all",
        shell=True,
        text=True,
        errors="ignore"
    )
    allow_count = result.count("Allow")
    block_count = result.count("Block")

    print("Firewall Analysis Report")
    print("------------------------")
    print("Allow Rules:", allow_count)
    print("Block Rules:", block_count)

    with open("firewall_report.txt", "w", encoding="utf-8") as file:
        file.write("FIREWALL ANALYSIS REPORT\n")
        file.write("========================\n")
        file.write(f"Allow Rules: {allow_count}\n")
        file.write(f"Block Rules: {block_count}\n")

    print("\nReport saved as firewall_report.txt")

except Exception as e:
    print("Error:", e)