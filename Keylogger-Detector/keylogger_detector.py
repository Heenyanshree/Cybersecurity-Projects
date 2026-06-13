import psutil

print("================================")
print("      KEYLOGGER DETECTOR")
print("================================")

suspicious_keywords = [
    "keylogger",
    "logger",
    "hook",
    "spy",
    "monitor"
]

found = False

print("\nScanning running processes...\n")

for process in psutil.process_iter(['pid', 'name']):
    try:
        process_name = process.info['name'].lower()

        for keyword in suspicious_keywords:
            if keyword in process_name:
                found = True
                print(f"ALERT: Suspicious Process Found")
                print(f"PID: {process.info['pid']}")
                print(f"Name: {process.info['name']}\n")

    except:
        pass

if not found:
    print("No suspicious processes detected.")