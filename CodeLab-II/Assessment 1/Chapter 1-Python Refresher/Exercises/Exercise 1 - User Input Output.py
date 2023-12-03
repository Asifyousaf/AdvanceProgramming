# Printing a Welcome msg.
print("Hello, user!")

# Asking the user to enter their name and convert it to title case.
user_name = str(input("what is your name?\n"))
name_title = user_name.title()

# Asking the user to enter their age.
user_age = int(input("what is your age?\n"))

# Printing a message using User name.
print(f"It is good to meet you, {name_title}")

# Calculating and printing the length of the user name
name_len = len(name_title)
print(f"The Length of your name is:\n{name_len}")

# Calculating and printing the age after one year
age_next_year = user_age + 1
print(f"You will be {age_next_year} in a year.")




