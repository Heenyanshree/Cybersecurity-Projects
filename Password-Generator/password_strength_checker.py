import re

print("================================")
print("   PASSWORD STRENGTH CHECKER")
print("================================")

password = input("Enter Password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search("[A-Z]", password):
    strength += 1

if re.search("[a-z]", password):
    strength += 1

if re.search("[0-9]", password):
    strength += 1

if re.search("[!@#$%^&*]", password):
    strength += 1

if strength <= 2:
    print("\nWeak Password")
elif strength <= 4:
    print("\nMedium Password")
else:
    print("\nStrong Password")