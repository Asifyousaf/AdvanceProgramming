# Chapter 4 Exercise 2 - CountString

# using the tkinter library
from tkinter import *


def count_string_occurrences(search_string, file_path):
    # Count occurrences of a specified string in a file and return a formatted result.
    # search_string (str): The string to search for.
    # file_path (str): The path to the file containing the text.
    try:
        # to open and read the specified file
        with open('Chapter 4 - File Handling and Regular Expressions/Exercises/Exercise 2 - CountString/sentences.txt', 'r') as file:
            content = file.read()
            
            # Counting occurrences of the search string
            count = content.lower().count(search_string.lower())
            
            # Return the result message
            return f'The string "{search_string}" appears {count} times.\n'
    except FileNotFoundError:
        # to handle the case where the file is not found
        return "File not found. Please make sure the file exists."

def submit_form():
    # Callback function for the submit button.
    # Go through a list of search strings, count their occurrences

    # List of strings to search for
    search_strings = [
        "Hello my name is Peter Parker",
        "I love Python Programming",
        "Love",
        "Enemy"
    ]

    result_text = ""
    
    # go through the search strings and count occurrences
    for search_string in search_strings:
        result_text += count_string_occurrences(search_string, 'sentences.txt') + '\n'

    # Updating the label with the result text
    result_label.config(text=result_text)

# Creating the main window
root = Tk()

# Setting the window size
root.geometry("360x200")

# Setting the title for the window
root.title("String Occurrences Counter")

# Button to submit the form
submit_button = Button(root, text="Find String Occurrences", command=submit_form,bg='#22263d',fg='white')
submit_button.pack(pady=10)

# Label to display the result
result_label = Label(root, text="",font=("Arial", 9, "bold"))
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()

# End Marker
