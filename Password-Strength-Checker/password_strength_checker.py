import re

print("================================")
print("   PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter Password: ")

score = 0

# Length
if len(password) >= 8:
    score += 1

# Uppercase
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase
if re.search(r"[a-z]", password):
    score += 1

# Number
if re.search(r"\d", password):
    score += 1

# Special Character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

print("\nPassword Analysis")
print("-----------------")

print("Length:", len(password))

if score <= 2:
    print("Strength : Weak")
elif score == 3 or score == 4:
    print("Strength : Medium")
else:
    print("Strength : Strong")

print("\nRecommendations")

if len(password) < 8:
    print("- Use at least 8 characters.")

if not re.search(r"[A-Z]", password):
    print("- Add uppercase letters.")

if not re.search(r"[a-z]", password):
    print("- Add lowercase letters.")

if not re.search(r"\d", password):
    print("- Add numbers.")

if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("- Add special characters.")