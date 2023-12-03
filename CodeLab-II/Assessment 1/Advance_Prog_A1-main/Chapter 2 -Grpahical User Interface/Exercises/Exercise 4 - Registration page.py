from tkinter import Tk, Label, PhotoImage

# Creating a root window
root = Tk()

# Setting the title for the window
root.title('Registration Page')

# Setting the size of the window
root.geometry('700x800')

# Adding background color to the window
root.configure(bg="white")

# Creating a label for the image
banner = PhotoImage(file='Advance_Prog_A1-main\Chapter 2 -Grpahical User Interface\Exercises\RAK.png', width=800, height=200)
banner_lbl = Label(root, image=banner, bg="#22263d")

# Using pack to center the image in the window
banner_lbl.pack(side=TOP)

root.mainloop()
