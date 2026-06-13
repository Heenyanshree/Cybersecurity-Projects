print("================================")
print("      AI PHISHING DETECTOR")
print("================================")

url = input("Enter URL: ")

risk_score = 0
reasons = []

if url.startswith("http://"):
    risk_score += 2
    reasons.append("Uses HTTP instead of HTTPS")

if "@" in url:
    risk_score += 2
    reasons.append("Contains @ symbol")

if "-" in url:
    risk_score += 1
    reasons.append("Contains hyphen")

if url.count(".") > 3:
    risk_score += 1
    reasons.append("Too many dots/subdomains")

if len(url) > 75:
    risk_score += 2
    reasons.append("URL is too long")

suspicious_words = ["login", "verify", "update", "secure", "account", "bank", "free", "password"]

for word in suspicious_words:
    if word in url.lower():
        risk_score += 1
        reasons.append(f"Contains suspicious word: {word}")

print("\nAI Analysis Report")
print("------------------")
print("Risk Score:", risk_score)

if risk_score <= 2:
    result = "Safe"
elif risk_score <= 5:
    result = "Suspicious"
else:
    result = "Phishing"

print("Prediction:", result)

print("\nReasons:")
if reasons:
    for reason in reasons:
        print("-", reason)
else:
    print("- No suspicious pattern found")

with open("ai_phishing_report.txt", "w") as file:
    file.write("AI PHISHING DETECTION REPORT\n")
    file.write("============================\n")
    file.write(f"URL: {url}\n")
    file.write(f"Risk Score: {risk_score}\n")
    file.write(f"Prediction: {result}\n\n")
    file.write("Reasons:\n")

    for reason in reasons:
        file.write(f"- {reason}\n")

print("\nReport saved as ai_phishing_report.txt")