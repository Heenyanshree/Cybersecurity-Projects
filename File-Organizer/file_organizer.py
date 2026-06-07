import os
import shutil

print("================================")
print("        FILE ORGANIZER")
print("================================")

folder_path = input("Enter folder path to organize: ")

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        extension = file_name.split(".")[-1]

        target_folder = os.path.join(folder_path, extension.upper())

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        shutil.move(file_path, os.path.join(target_folder, file_name))

print("\nFiles organized successfully!")