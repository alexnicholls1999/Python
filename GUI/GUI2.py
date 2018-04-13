from tkinter import *

root = Tk()

one = Label(root, text="One", bg= "white", fg="black")
one.pack()
two = Label(root, text="two", bg= "white", fg="black")
two.pack(fill=X)
three = Label(root, text="Three", bg= "white", fg="black")
three.pack(side=LEFT, fill=Y)


root.mainloop()
