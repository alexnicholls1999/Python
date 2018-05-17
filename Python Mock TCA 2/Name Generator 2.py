from tkinter import *
from tkinter import messagebox


class NameGenerator(Tk): 
    def __init__(self):
        Tk.__init__(self)
       
        # Style for Window

       
        
        # Add Components 
        self.add_header_label()
        self.add_fname()
        self.add_lname()
        self.add_buttons()

    def add_header_label(self):

        # Label Add 
        self.header_label = Label(text="Name Maker")
        self.header_label.pack(fill=X)

        # styling 
        self.header_label.configure(font="Arial 18", padx=50, pady=10)

    def add_fname(self):
        self.name_frame = Frame()
        self.name_frame.pack()
        
        # Entry Add 
        self.name_entry = Entry(self.name_frame, width=30)
        self.name_entry.pack(side=RIGHT)

        # Label Add 
        self.name_label = Label(self.name_frame, text="Your Name:")
        self.name_label.pack(side=LEFT)

        # styling 
        self.name_label.configure(font="Arial 10", padx=25, pady=10)

    def add_lname(self):
        self.lname_frame = Frame()
        self.lname_frame.pack()
        
        # Entry Add 
        self.lname_entry = Entry(self.lname_frame, width=30)
        self.lname_entry.pack(side=RIGHT)

        # Label Add 
        self.lname_label = Label(self.lname_frame, text="Your Last Name:")
        self.lname_label.pack(side=LEFT)

        # styling 
        self.lname_label.configure(font="Arial 10", padx=10, pady=10)

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
        first_name = self.name_entry.get()
        last_name = self.lname_entry.get()
        message = "Hello " + first_name + " " + last_name

        if first_name and last_name != " ":
            messagebox.showinfo('Name Generator!', message)
        else: 
            messagebox.showerror("Name Generator: Error!", "No name entered")

gui = NameGenerator()
gui.mainloop()