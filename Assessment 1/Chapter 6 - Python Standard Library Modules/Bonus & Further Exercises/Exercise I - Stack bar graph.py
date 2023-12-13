# Chapter 5 Further Exercise I - Stack Bar Graph

import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title('Super Bowl Watching Preferences by Gender')

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Data from the table
categories = ['Game', 'Commercials', "Won't Watch"]
male_responses = [279, 81, 132]
female_responses = [200, 156, 160]

# Calculate the maximum number of responses for scaling
max_responses = max(max(male_responses), max(female_responses))

# Set the bar width and gap between bars
bar_width, bar_gap = 30, 20

# Draw stacked bars for male and female responses
for i, category in enumerate(categories):
    x = 50 + i * (bar_width + bar_gap)
    y_bottom, height = 250, 150

    y_top_male = y_bottom - (male_responses[i] / max_responses) * height
    y_top_female = y_bottom - ((male_responses[i] + female_responses[i]) / max_responses) * height

    # Draw male response bar
    canvas.create_rectangle(x, y_bottom, x + bar_width, y_top_male, fill='blue', outline='black')
    canvas.create_text(x + bar_width / 2, y_bottom + 10, text=str(male_responses[i]))

    # Draw female response bar on top of male response bar
    canvas.create_rectangle(x, y_top_male, x + bar_width, y_top_female, fill='pink', outline='black')
    canvas.create_text(x + bar_width / 2, y_top_female + 10, text=str(female_responses[i]))

# Adding labels and title
labels = ['Response Categories', 'Number of Responses', 'Super Bowl Watching Preferences by Gender']
positions = [(200, 280), (30, 150), (200, 20)]

for label, (x, y) in zip(labels, positions):
    canvas.create_text(x, y, text=label, font=('Helvetica', 10), angle=90 if label == 'Number of Responses' else 0)

# Adding legend
legend_labels = ['Male', 'Female']
legend_colors = ['blue', 'pink']

for label, color, x in zip(legend_labels, legend_colors, [300, 350]):
    canvas.create_text(x, 180, text=label, font=('Helvetica', 10), fill=color)

# Run the Tkinter event loop
root.mainloop()
