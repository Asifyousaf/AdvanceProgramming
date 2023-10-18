import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=800,height=600)
line = canvas.create_oval(10,10,130,100, fill="red",outline="black", width=2)
canvas.pack()
root.mainloop()
