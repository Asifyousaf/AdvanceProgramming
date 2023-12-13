# Chapter 2 Further Exercise I - Count Characters

# using the tkinter library
from tkinter import *

def count():
    user_input = sentence_entry.get().lower()
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    specials = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'
    
    vowel_count = 0
    consonant_count = 0
    special_count = 0

    for char in user_input:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char in specials:
            special_count += 1

    total_letters = vowel_count + consonant_count

    result_label.config(text=f"Number of vowels: {vowel_count}\nNumber of consonants: {consonant_count}\nNumber of special characters: {special_count}\nTotal number of letters: {total_letters}")

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Character Counter")

# Adding a white background to the main window
root.configure(bg='#FFFFFF')

# Heading
heading_label = Label(root, font=('Roboto', 20, 'bold'), text="Character Counter", bg='#FFFFFF', fg='#22263d')
heading_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Input label and entry
input_label = Label(root, text="Enter a sentence:", font=('Roboto', 12, 'bold'), bg='#FFFFFF', fg='#22263d')
input_label.grid(row=1, column=0, pady=10, padx=10)

sentence_entry = Entry(root, font=('Roboto', 12), bg='#B0C4DE', fg='#000000')
sentence_entry.grid(row=1, column=1, pady=10, padx=10)

# Button to count characters
count_button = Button(root, text="Count Characters", command=count, font=('Roboto', 12, 'bold'), bg='#22263d', fg='#FFFFFF')
count_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result
result_label = Label(root, text="", font=('Roboto', 12, 'bold'), bg='#FFFFFF', fg='#000000')
result_label.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

# Start the Tkinter event loop
root.mainloop()

#End marker