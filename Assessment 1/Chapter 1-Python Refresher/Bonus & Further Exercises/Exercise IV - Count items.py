# Chapter 1 Further Exercise IV - Count items

# List of staff members
staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Rafia", "Mary", "Anmol", 
         "Zainab", "Iftikhar", "Arshiya", "Rafia", "Jake"]

# Dictionary to store the count of each staff member
staff_count = {}

# To Go through each staff member in the list
for item in staff:
    # Checking if the current staff member already exists in the dictionary.
    if item in staff_count:
        # If the staff member exists increment their count by 1
        staff_count[item] += 1
    else:
        # If the staff member does not exist add them to the dictionary with a count of 1
        staff_count[item] = 1

# Printing the counts for each staff member
for key, value in staff_count.items():
    print(f"{key}: {value} times")

# End marker