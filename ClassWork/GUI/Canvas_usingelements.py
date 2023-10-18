import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=800,height=800)
oval=canvas.create_oval(170,180,300,310, fill="red",outline="white", width=2)
box = canvas.create_rectangle(70,80,100,110, fill="yellow", width=2)
text= canvas.create_text(140,30,text="CANVAS ELEMENTS",font=("arial",14),fill="green")
canvas.pack()
root.mainloop()