# Import the json module to work with JSON data
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

# Opening the JSON file in write mode and save the student details as JSON
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

# Step 3: Append and update the JSON file

# Creating a dictionary with additional course details
course_details = {
    "CourseDetails": {
        "Group": "A",
        "Year": 2   
    }
}

# Step 3 and 4: Update and read the JSON file
with open(file_path, 'r') as json_file:
    existing_data = json.load(json_file)
    existing_data["StudentDetails"].update(course_details["CourseDetails"])

# Reopen the file in write mode to save the updated data
with open(file_path, 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)

# Step 4: Read and print the updated values

# Opening the JSON file in read mode
with open(file_path, 'r') as json_file:
    # Load the updated JSON data from the file into a Python dictionary
    updated_data = json.load(json_file)

    # Print the details of the student, including the updated course details
    print("\nDetails of the Student are")
    for key, value in updated_data["StudentDetails"].items():
        print(f"\t{key}: {value}")


# End marker
