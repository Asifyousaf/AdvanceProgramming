import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=800,height=600)
line = canvas.create_line(50,70,100,70, fill="red", width=2)
canvas.pack()
root.mainloop()