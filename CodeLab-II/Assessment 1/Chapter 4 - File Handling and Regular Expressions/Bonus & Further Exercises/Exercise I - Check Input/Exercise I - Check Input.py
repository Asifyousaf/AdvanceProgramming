# using the tkinter library
from tkinter import *

# Function to check if the input contains only letters, numbers, and underscores
def check_letters_numbers_underscores(input_text):
    # Matching a string that contains only upper and lowercase letters, numbers, and underscores
    return "Match found!" if input_text.isalnum() or '_' in input_text else "No match found."

# Function to check if the input starts with a number
def check_start_with_number(input_text):
    # Matching a string that starts with a specific number
    return "Match found!" if input_text[0].isdigit() else "No match found."

# Function to check if the input contains a specific substring
def check_substrings(input_text):
    # Find substrings within a string
    return "Match found!" if "substring" in input_text else "No match found."

# Function to check if the input starts with a specific word
def check_word_at_beginning(input_text):
    # Match a word at the beginning of a string
    return "Match found!" if input_text.startswith("Word") else "No match found."

# Function to handle button click
def on_button_click(check_function, entry_widget, result_label):
    input_text = entry_widget.get()
    result_text = check_function(input_text)
    result_label.config(text=result_text)

# Creating the main window
root = Tk()

root.title("Input Checker")
root.geometry('300x300')

# The heading label
welcome_label = Label(root, text="Input checker", font=("Roboto", 18, "bold"))
welcome_label.pack(pady=10)

# Entry for user input
input_entry = Entry(root)
input_entry.pack(pady=10)

# Result label
result_label = Label(root, text="")
result_label.pack(pady=10)

# Button for "Letters, Numbers, Underscores"
button1 = Button(root, text="Letters, Numbers, Underscores", command=lambda: on_button_click(check_letters_numbers_underscores, input_entry, result_label), bg="blue", fg="white")
button1.pack(pady=5)

# Button for "Starts with Number"
button2 = Button(root, text="Starts with Number", command=lambda: on_button_click(check_start_with_number, input_entry, result_label), bg="blue", fg="white")
button2.pack(pady=5)

# Button for "Substrings"
button3 = Button(root, text="Substrings", command=lambda: on_button_click(check_substrings, input_entry, result_label), bg="blue", fg="white")
button3.pack(pady=5)

# Button for "Word at the Beginning"
button4 = Button(root, text="Word at the Beginning", command=lambda: on_button_click(check_word_at_beginning, input_entry, result_label), bg="blue", fg="white")
button4.pack(pady=5)

# Run the main event loop
root.mainloop()

# End marker