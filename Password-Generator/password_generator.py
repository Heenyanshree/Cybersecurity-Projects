import random
import string

print("================================")
print("      PASSWORD GENERATOR")
print("================================")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)

save = input("\nSave password to file? (y/n): ")

if save.lower() == "y":
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")
    print("Password saved successfully!")