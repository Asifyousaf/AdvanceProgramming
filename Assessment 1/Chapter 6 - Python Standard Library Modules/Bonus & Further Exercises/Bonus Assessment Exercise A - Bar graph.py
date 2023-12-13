# Chapter 6 Bonus Exercise A - Bar Grapgh

import tkinter as tk

def draw_bar(x, y_bottom, y_top, brand, value):
    canvas.create_rectangle(x, y_bottom, x + bar_width, y_top, fill='skyblue', outline='black')
    canvas.create_text((x + x + bar_width) / 2, y_bottom + 10, text=f"{brand}\n{value}")

# Create a Tkinter window
root = tk.Tk()
root.title("Most Valuable Brands Worldwide in 2023")

# Create a Canvas widget
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

# Information for the bar graph
title = "Most valuable brands worldwide in 2023 (in billion U.S. dollars)"
brands = ["Amazon", "Apple", "Google", "Microsoft", "Walmart", "Samsung Group", "ICBC", "Verizon", "Tesla", "TikTok/Douyin"]
values = [299.28, 297.51, 281.38, 191.57, 113.78, 99.66, 69.55, 67.44, 66.21, 65.67]  # Given Data

# Normalize values for better visualization
max_value = max(values)
normalized_values = [v / max_value * 200 for v in values]

# Set bar width and gap
bar_width, bar_gap = 30, 20

# Draw bars for each brand without using loops
x, y_bottom = 50, 250

draw_bar(x, y_bottom, y_bottom - normalized_values[0], brands[0], values[0])

x += (bar_width + bar_gap)
draw_bar(x, y_bottom, y_bottom - normalized_values[1], brands[1], values[1])

# Adding labels and title
canvas.create_text(250, 20, text=title, font=('Helvetica', 12), anchor='center')
canvas.create_text(250, 280, text='Brands', font=('Helvetica', 10), anchor='center')
canvas.create_text(20, 150, text='Brand Value (in billion U.S. dollars)', font=('Helvetica', 10), angle=90, anchor='center')

# Run the Tkinter event loop
root.mainloop()
