# using the tkinter library,random and messagebox
from tkinter import *
import random
from tkinter import messagebox

# Global variable to store the current word for the user to guess
current_word = ""

def check_guess():
    # Getting the user's guess from the entry field and convert it to lowercase
    guess = entry.get().lower()

    # Check if the guess is correct
    if guess == current_word.lower():
        messagebox.showinfo('Result', 'Whoa, you nailed it! Great job!')
        update_score()
        new_word()  # Generating a new word for the user to guess
    else:
        # Showing the result message first, then update current_word
        messagebox.showinfo('Result', f"Oops, not quite! The answer is {current_word}.")
        new_word()  # Generating a new word for the user to guess

def update_score():
    # Extracting the current score from the label text and increment it
    current_score = int(score_label["text"].split(":")[-1])
    score_label.config(text=f'Your Score: {current_score + 1}')

def new_word():
    # Declaring current_word as global to update the global variable
    global current_word  

    # Selecting a random word from the list
    word = random.choice(words)

    # Shuffling the characters of the word for a bit of fun
    shuffle_word = random.sample(word, len(word))

    # Displaying the shuffled word in the label
    shuffle_label.config(text='Can you unscramble this: ' + ' '.join(shuffle_word))

    current_word = word  # Update the global variable with the new word

# Listing of words for the user to guess
words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pineapple', 'raspberry', 'strawberry', 'tomato', 'watermelon']

# Creating the main window
root = Tk()

# Setting the title of the window
root.title('Word Guessing Game')

# Setting the window size
root.geometry("400x300")

# Creating a frame within the window with padding
frame = Frame(root, padx=20, pady=20)  
frame.pack()

# Creating an entry widget for the user to input their guess
entry = Entry(frame, font=('Calibri', 14), fg='#212121')  
entry.pack(pady=10)

# Creating a blue-colored button with a different font for checking the guess
check_button = Button(frame, text='Check Guess', command=check_guess, bg='#2196F3', fg='#FFFFFF', font=('Calibri', 12, 'bold'))
check_button.pack(pady=10)

# Creating a blue-colored button with a different font for getting a new word
new_word_button = Button(frame, text='New Word', command=new_word, bg='#2196F3', fg='#FFFFFF', font=('Calibri', 12, 'bold'))
new_word_button.pack(pady=10)

# Creating a label to display the shuffled word for the user to unscramble
shuffle_label = Label(frame, text='Can you unscramble this: ', font=('Calibri', 14), bg='#E3F2FD', fg='#212121')
shuffle_label.pack(pady=10)

# Creating a label to display the user's current score
score_label = Label(frame, text='Your Score: 0', font=('Calibri', 14), bg='#E3F2FD', fg='#212121')
score_label.pack(pady=10)

# Initializing the current_word variable with a new word
new_word()

# Starting the main event loop
root.mainloop()

# End marker