from tkinter import *
from tkinter import messagebox


class NameGenerator(Tk): 
    def __init__(self):
        Tk.__init__(self)
       
        # Style for Window

       
        
        # Add Components 
        self.add_header_label()
        self.add_name_label()
        self.add_name_entry()
        self.add_buttons()

    def add_header_label(self):

        # Label Add 
        self.header_label = Label(text="Name Maker")
        self.header_label.pack(fill=X)

        # styling 
        self.header_label.configure(font="Arial 18", padx=50, pady=10)

    def add_name_label(self):

        # Label Add 
        self.name_label = Label(text="Your Name:")
        self.name_label.pack(anchor=W)

        # styling 
        self.name_label.configure(font="Arial 10", padx=10, pady=10)
        
    def add_name_entry(self):

        self.name_frame = Frame()
        self.name_frame.pack()

        # Label Add 
        self.name_entry = Entry(self.name_frame, width=35)
        self.name_entry.pack(side=LEFT)
        
    def add_buttons(self):

        # frame
        self.btn_frame = Frame()
        self.btn_frame.pack()
    
        # convert button 
        self.btn_generate = Button(self.btn_frame, text="Generate")
        self.btn_generate.pack(pady=10)


        # Bind 
        self.btn_generate.bind("<ButtonRelease-1>", self.message)


    def message(self, event):
        message = self.name_entry.get()

        if message != "":
            messagebox.showinfo('Name Generator: Error!', "Hello %s" % message)
        else: 
            messagebox.showerror("Name Generator: Error!", "No name entered")

gui = NameGenerator()
gui.mainloop()