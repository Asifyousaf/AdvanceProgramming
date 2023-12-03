staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

staff_count = {}

for item in staff:
    # Check if the current staff member already exists in the dictionary.
    if item in staff_count:
        # If the staff member exists, increment their count by 1.
        staff_count[item] += 1
    else:
        # If the staff member does not exist, add them to the dictionary with a count of 1.
        staff_count[item] = 1

print(staff_count{key})