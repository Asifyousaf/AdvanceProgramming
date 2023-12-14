import json

# Specify the file path
file_path = 'StudentJson.json'

# Step 1: Ask the user to enter student details and write to JSON file

# Create a dictionary to store the user's input for student details
student_details = {
    "Name": input("Enter student name: "),
    "ID": int(input("Enter student ID: ")),
    "course": input("Enter student course: ")
}

try:
    # Opening the JSON file in read and append mode
    with open(file_path, 'w+') as json_file:
        # Move the file pointer to the beginning before reading
        json_file.seek(0)

        # Load the existing JSON data from the file into a Python dictionary
        try:
            existing_data = json.load(json_file)
        except json.JSONDecodeError:
            existing_data = {}

        # Update existing_data with new student details
        existing_data["StudentDetails"] = student_details

        # Move the file pointer to the beginning before writing
        json_file.seek(0)

        # Write the updated data to the file
        json.dump(existing_data, json_file, indent=4)
except FileNotFoundError:
    # Handle the case when the file doesn't exist
    with open(file_path, 'w') as json_file:
        json.dump({"StudentDetails": student_details}, json_file, indent=4)

# Step 2: Read and display the individual values

# Opening the JSON file in read mode
with open(file_path, 'r') as json_file:
    # Load the JSON data from the file into a Python dictionary
    data = json.load(json_file)

    # Print the details of the student
    print("\nDetails of the Student are")
    for key, value in data["StudentDetails"].items():
        print(f"\t{key}: {value}")
