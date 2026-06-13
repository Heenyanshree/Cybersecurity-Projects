import hashlib

print("================================")
print("      FILE INTEGRITY CHECKER")
print("================================")

file_name = input("Enter file name: ")

def calculate_hash(filename):
    with open(filename, "rb") as file:
        data = file.read()
        hash_value = hashlib.sha256(data).hexdigest()
        return hash_value

current_hash = calculate_hash(file_name)

try:
    with open("hash_record.txt", "r") as file:
        old_hash = file.read()

    if current_hash == old_hash:
        print("File is safe. No changes detected.")
    else:
        print("ALERT: File has been modified!")

except FileNotFoundError:
    with open("hash_record.txt", "w") as file:
        file.write(current_hash)

    print("Hash saved for the first time.")