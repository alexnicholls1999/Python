from tkinter import *

def doNothing():
    print("Creating New Document...")
def Quit():
    global root
    root.destroy()

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_command(label="Save", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=Quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

root.mainloop()
