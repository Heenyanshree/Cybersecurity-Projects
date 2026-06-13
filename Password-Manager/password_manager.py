print("================================")
print("       PASSWORD MANAGER")
print("================================")

while True:

    print("\n1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        with open("passwords.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")

        print("Password Saved!")

    elif choice == "2":

        print("\nSaved Passwords:")
        print("----------------")

        with open("passwords.txt", "r") as file:
            print(file.read())

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")