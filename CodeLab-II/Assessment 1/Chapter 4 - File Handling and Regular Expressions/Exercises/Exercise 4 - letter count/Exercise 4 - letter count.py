# Importing the tkinter library for GUI
from tkinter import *

# Function to count occurrences of a character in a file
def count_occurrences(character, file_path):
    try:
        # Opening and reading the specified file
        with open('sentences.txt', 'r') as file:
            content = file.read()
            # Counting occurrences of the character (case-insensitive)
            count = content.lower().count(character.lower())
            return f'The letter "{character}" appears {count} times.'
    except FileNotFoundError:
        return "File not found. Please make sure the file exists."

# Function to handle form submission
def submit_form():
    # Getting user input from the entry field
    user_input = entry_character.get()
    # Counting occurrences and updating the result label
    result_text = count_occurrences(user_input, 'sentences.txt')
    result_label.config(text=result_text)

# Creating the main window
root = Tk()

# Setting the window size 
root.title("Letter Occurrences Counter")

# Setting the window size 
root.geometry("400x200")

# Label and Entry for user input
label_prompt = Label(root, text="Enter a character:")
label_prompt.pack(pady=10)

entry_character = Entry(root)
entry_character.pack(pady=10)

# Button to submit the form
submit_button = Button(root, text="Count Occurrences", command=submit_form)
submit_button.pack(pady=10)

# Label to display the result
result_label = Label(root, text="")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()

