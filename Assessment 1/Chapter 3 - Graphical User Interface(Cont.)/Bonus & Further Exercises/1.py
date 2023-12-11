import tkinter as tk
import random

class GuessWordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Word Game")

        self.words = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "GITHUB", "PROGRAMMING", "PYTHONIC"]
        self.score = 0
        self.current_word = ""
        self.time_left = 30  # You can extend this for different levels

        # Widgets
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Helvetica", 16))
        self.score_label.pack(pady=10)

        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 16))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 14))
        self.submit_button.pack(pady=20)

        # Timer
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left} s", font=("Helvetica", 14))
        self.timer_label.pack()

        # Start the game
        self.next_word()
        self.update_timer()

    def next_word(self):
        self.current_word = random.choice(self.words)
        shuffled_word = "".join(random.sample(self.current_word, len(self.current_word)))
        self.word_label.config(text=shuffled_word)

    def check_answer(self):
        user_guess = self.answer_entry.get().upper()

        if user_guess == self.current_word:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.next_word()
            self.answer_entry.delete(0, tk.END)
        else:
            self.answer_entry.delete(0, tk.END)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left} s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.word_label.config(text="Game Over!")
        self.answer_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.geometry("400x300")

# Initialize and run the game
game = GuessWordGame(root)

# Start the Tkinter event loop
root.mainloop()
