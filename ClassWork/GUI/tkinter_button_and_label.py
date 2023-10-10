from tkinter import *
#create a root window 
root = Tk()
# Main loop 
root.title('Widgets example')

root.geometry('600x600')

root.resizable(0,0)
mybutton = Button(root, text="Button")
mylabel = Label(root, text="WELCOME")
mylabel.pack()
mybutton.pack()
root.mainloop()
