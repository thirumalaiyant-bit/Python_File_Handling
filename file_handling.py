import os
import csv
import shutil

# Write data into a text file
try:
    with open("sample.txt", "w") as file:
        file.write("Hello! This is a Python file handling program.\n")
        file.write("Python can read and write files easily.")

    print("Text file created and written successfully.")

except Exception as e:
    print("Error while writing text file:", e)
    # Read data from the text file
try:
    with open("sample.txt", "r") as file:
        content = file.read()

    print("\nContent of sample.txt:")
    print(content)

except FileNotFoundError:
    print("sample.txt was not found.")
    # Write data into a CSV file
try:
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Age", "Department"])
        writer.writerow(["Pavi", 18, "ECE"])
        writer.writerow(["Anu", 18, "EEE"])
        writer.writerow(["Priya", 19, "CSE"])

    print("\nCSV file created successfully.")

except Exception as e:
    print("Error while creating CSV:", e)
    # Read data from CSV file
try:
    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        print("\nStudent details:")

        for row in reader:
            print(row)

except FileNotFoundError:
    print("students.csv was not found.")
    # Rename the text file
try:
    os.rename("sample.txt", "renamed_sample.txt")
    print("\nFile renamed successfully.")

except FileNotFoundError:
    print("File to rename was not found.")

except FileExistsError:
    print("The new file name already exists.")
    # Move the renamed file into a folder
try:
    os.makedirs("Moved_Files", exist_ok=True)

    shutil.move("renamed_sample.txt", "Moved_Files/renamed_sample.txt")

    print("File moved successfully.")

except FileNotFoundError:
    print("File to move was not found.")
    # Create and delete a temporary file
try:
    with open("delete_me.txt", "w") as file:
        file.write("This file will be deleted.")

    os.remove("delete_me.txt")

    print("Temporary file deleted successfully.")

except FileNotFoundError:
    print("File to delete was not found.")
    # Program completed
print("\nFile handling and automation completed successfully!")
   