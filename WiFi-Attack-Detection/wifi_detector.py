print("================================")
print("     WIFI ATTACK DETECTOR")
print("================================")

wifi_name = input("Enter Wi-Fi Name (SSID): ")

suspicious_words = [
    "free",
    "public",
    "hack",
    "wifi",
    "airport",
    "guest"
]

risk = 0

for word in suspicious_words:
    if word in wifi_name.lower():
        risk += 1

print("\nWi-Fi Analysis Report")
print("----------------------")
print("SSID:", wifi_name)

if risk == 0:
    print("Result: Safe Network")
elif risk <= 2:
    print("Result: Suspicious Network")
else:
    print("Result: High Risk Network")