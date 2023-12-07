import tkinter as tk
import re

def check_input(pattern, input_text):
    # Check if the input matches the pattern using fullmatch
    match = pattern.fullmatch(input_text)
    if match:
        return "Match found!"
    else:
        return "No match found."

def on_button_click(pattern, entry_widget, result_label):
    input_text = entry_widget.get()
    result_text = check_input(pattern, input_text)
    result_label.config(text=result_text)

# Creating the main window
root = tk.Tk()
root.title("Input Checker")

# Entry for user input
input_entry = tk.Entry(root)
input_entry.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Patterns for different regular expression options
patterns = [
    ("Letters, Numbers, Underscores", re.compile(r'^\w+$')),
    ("Starts with Number", re.compile(r'^\d.*')),
    ("Substrings", re.compile(r'.*substring.*')),
    ("Word at the Beginning", re.compile(r'^Word.*')),
]

for pattern_name, pattern in patterns:
    button = tk.Button(root, text=pattern_name, command=lambda p=pattern: on_button_click(p, input_entry, result_label))
    button.pack()

# Run the main event loop
root.mainloop()
