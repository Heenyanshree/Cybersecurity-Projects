import re

print("================================")
print(" AI THREAT INTELLIGENCE PLATFORM")
print("================================")

filename = input("Enter threat feed file: ")

with open(filename, "r") as file:
    feeds = file.readlines()

ioc_count = 0
malware_count = 0
suspicious_count = 0

ip_addresses = []
domains = []
malware_names = []

print("\nThreat Intelligence Report")
print("--------------------------")

for item in feeds:
    item = item.strip()

    ip_match = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", item)
    domain_match = re.findall(r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", item)

    if ip_match:
        ip_addresses.extend(ip_match)

    if domain_match:
        domains.extend(domain_match)

    if "MALWARE" in item:
        malware_count += 1
        malware_name = item.replace("MALWARE", "").replace("detected", "").strip()
        malware_names.append(malware_name)
        print("[MALWARE]", item)

    elif "IOC" in item:
        ioc_count += 1
        print("[IOC]", item)

    elif "SUSPICIOUS" in item:
        suspicious_count += 1
        print("[SUSPICIOUS]", item)

risk_score = (ioc_count * 2) + (malware_count * 3) + suspicious_count

print("\nIOC Detection")
print("-------------")
print("IP Addresses:", ip_addresses)
print("Domains:", domains)
print("Malware Names:", malware_names)

print("\nSummary")
print("-------")
print("IOC Count:", ioc_count)
print("Malware Count:", malware_count)
print("Suspicious Count:", suspicious_count)
print("Risk Score:", risk_score)

if risk_score >= 10:
    print("Threat Level: HIGH")
elif risk_score >= 5:
    print("Threat Level: MEDIUM")
else:
    print("Threat Level: LOW")

with open("threat_intel_report.txt", "w") as report:
    report.write("AI THREAT INTELLIGENCE REPORT\n")
    report.write("=============================\n")
    report.write(f"IP Addresses: {ip_addresses}\n")
    report.write(f"Domains: {domains}\n")
    report.write(f"Malware Names: {malware_names}\n")
    report.write(f"IOC Count: {ioc_count}\n")
    report.write(f"Malware Count: {malware_count}\n")
    report.write(f"Suspicious Count: {suspicious_count}\n")
    report.write(f"Risk Score: {risk_score}\n")

print("\nReport saved as threat_intel_report.txt")