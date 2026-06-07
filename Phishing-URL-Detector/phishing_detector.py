print("================================")
print("      PHISHING URL DETECTOR")
print("================================")

url = input("Enter URL: ")

risk_score = 0

if "http://" in url:
    risk_score += 1

if "@" in url:
    risk_score += 1

if "-" in url:
    risk_score += 1

if url.count(".") > 3:
    risk_score += 1

if len(url) > 75:
    risk_score += 1

suspicious_words = ["login", "verify", "update", "secure", "account", "bank", "free"]

for word in suspicious_words:
    if word in url.lower():
        risk_score += 1

print("\nURL Analysis Report")
print("-------------------")
print("Risk Score:", risk_score)

if risk_score <= 1:
    print("Result: Safe URL")
elif risk_score <= 3:
    print("Result: Suspicious URL")
else:
    print("Result: Phishing URL")