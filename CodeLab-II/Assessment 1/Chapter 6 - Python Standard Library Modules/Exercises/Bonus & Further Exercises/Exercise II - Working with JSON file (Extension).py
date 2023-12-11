# Import the json module to work with JSON data
import json

# the file path
file_path = 'StudentJson.json'

# Function to get student details
def get_student_details():
    return {
        "Name": input("Enter student name: "),
        "ID": int(input("Enter student ID: ")),
        "course": input("Enter student course: ")
    }

# Step 1: Asking the user to enter details for the first student and write to JSON file
first_student_details = get_student_details()

# Adding CourseDetails for the first student
first_student_details["CourseDetails"] = {
    "Group": "A",
    "Year": 2
}

# Opening the JSON file in write mode and save the details of the first student
with open(file_path, 'w') as json_file:
    json.dump({"StudentDetails": first_student_details}, json_file, indent=4)

# Step 2: Reading and display the details of the first student
with open(file_path, 'r') as json_file:
    data = json.load(json_file)

    # Printing the details of the first student
    print("\nDetails of the First Student are")
    for key, value in data["StudentDetails"].items():
        print(f"\t{key}: {value}")

# Step 3: Appending and update the JSON file with details for a second student
second_student_details = get_student_details()

# Adding CourseDetails for the second student
second_student_details["CourseDetails"] = {
    "Group": "A",
    "Year": 2
}

# Opening the JSON file in read mode and load existing data
with open(file_path, 'r') as json_file:
    existing_data = json.load(json_file)

# Updating the existing data with details for the second student
existing_data["SecondStudentDetails"] = second_student_details


# Reopen the file in write mode to save the updated data
with open(file_path, 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)

# Step 4: Reading and print the updated values for all students
with open(file_path, 'r') as json_file:
    updated_data = json.load(json_file)
    print("\nDetails of the Students are")

    # Printing the details of all students, including the updated course details for both students
    for student, details in updated_data.items():
        print(f"\tStudent: {student}")
        for key, value in details.items():
            print(f"\t\t{key}: {value}")
