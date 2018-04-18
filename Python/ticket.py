import tkinter as t
from tkinter import messagebox

title,question,entry,buy = None, None, None, None 

def run():
        global title,question,entry,buy

        root = t.Tk()

        
        title = t.Label(text="Entrance Ticket")
        title.grid(row=0, column=1, sticky= 'W')
        question = t.Label(text="How Many Tickets Are Needed?")
        question.grid(row=1, column= 0)
        entry = t.Entry(root, width=80)
        entry.grid(row=2, column=0, columnspan=5, padx=10)
        buy = t.Button(text="Buy", width= 10, command=out)
        buy.grid(row=3, column=1, pady=10, sticky='W')

        root.mainloop()

def out():
    output = (entry.get())
    messagebox.showinfo("Kaunas Party GUI", output)

run()

#     def __init__(self):
#         Tk.__init__(self)

    
#     def mess(self):
#         output = str(self.entry)
#         messagebox.showinfo("Kaunas Party GUI", output)

# # Object 
# gui = KaunasPartyGui()
# gui.mainloop()
