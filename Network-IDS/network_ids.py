import pandas as pd
from sklearn.ensemble import RandomForestClassifier

print("================================")
print(" NETWORK INTRUSION DETECTION")
print("================================")

data = {
    "packet_size": [100, 120, 150, 1000, 1200, 1300, 90, 1400],
    "connection_count": [2, 3, 1, 80, 100, 120, 2, 150],
    "failed_logins": [0, 0, 0, 10, 20, 25, 0, 30],
    "label": [0, 0, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["packet_size", "connection_count", "failed_logins"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

packet_size = int(input("Enter packet size: "))
connection_count = int(input("Enter connection count: "))
failed_logins = int(input("Enter failed logins: "))

input_data = pd.DataFrame(
    [[packet_size, connection_count, failed_logins]],
    columns=["packet_size", "connection_count", "failed_logins"]
)

prediction = model.predict(input_data)

print("\nIDS Report")
print("----------")

if prediction[0] == 1:
    print("Result: Intrusion Detected")
else:
    print("Result: Normal Traffic")