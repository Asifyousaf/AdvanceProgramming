# using the tkinter library
from tkinter import *

# Create the main window
root = Tk()
root.title("Labels Inside Frames")

# Creating left frame and displaying it with pack
left_frame = Frame(root, bd=5, relief="groove")
left_frame.pack(side=LEFT, expand=True, fill=BOTH)

# Creating right frame and displaying it with pack
right_frame = Frame(root, bd=5, relief="groove")
right_frame.pack(side=RIGHT, expand=True, fill=BOTH)

# Creating labels A and B inside the left frame with style
label_a = Label(left_frame, text="A", bg="#22263d",fg="white", width=10, bd=5 )
label_b = Label(left_frame, text="B", bg="white", width=10, bd=5 )

# Using Pack labels A and B in the left frame 
label_a.pack(side=TOP, expand=True, fill=BOTH)
label_b.pack(side=BOTTOM, expand=True, fill=BOTH)

# Creating labels C and D inside the right frame
label_c = Label(right_frame, text="C", bg="white", width=10, bd=5)
label_d = Label(right_frame, text="D", bg="#22263d",fg="white", width=10, bd=5, )

# Packing labels C and D in the right frame
label_c.pack(side=TOP, expand=True, fill=BOTH)
label_d.pack(side=BOTTOM, expand=True, fill=BOTH)

# Start the Tkinter event loop
root.mainloop()

# End marker