from tkinter import *

# Create a Tkinter window
root = Tk()
root.title('Line Graph Exercise')

# Create a Canvas widget
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# Draw Line 1: From (50, 50) to (300, 250)
canvas.create_line(50, 50, 300, 250, fill='blue', width=2, tags='line1')

# Draw Line 2: Dotted line from (50, 75) to (100, 250) to (300, 25) to (400, 300)
canvas.create_line(50, 75, 100, 250, 300, 25, 400, 300, fill='red', width=2, dash=(4, 4), tags='line2')

# Adding labels
canvas.create_text(200, 280, text='X-axis', font=('Helvetica', 10))
canvas.create_text(30, 150, text='Y-axis', font=('Helvetica', 10), angle=90)

# Adding legend
canvas.create_text(350, 50, text='Line 1', font=('Helvetica', 10), fill='blue')
canvas.create_text(350, 75, text='Line 2', font=('Helvetica', 10), fill='red')

# Run the Tkinter event loop
root.mainloop()
