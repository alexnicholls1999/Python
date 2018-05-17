from tkinter import *
from tkinter import messagebox


class BMI(Tk): 
    def __init__(self):
        Tk.__init__(self)

        # Add Tk Components 
        self.add_header_label()    
        self.add_name_label()
        self.add_name_entry()
        self.add_height_label()
        self.add_height_entry()
        self.add_weight_label()
        self.add_weight_entry()
        self.add_buttons()
        self.add_text_block()

        self.configure(background="#ffe8e8")
    def add_header_label(self):
        # Adding Label
        self.header_label = Label(text="Personal BMI Calculator")
        self.header_label.pack(fill=X)

        # Styling 
        self.header_label.configure(font="Arial 18", padx=50, pady=10, bg="#ffe8e8")

    def add_name_label(self):

        # Frame
        self.name_frame = Frame()
        self.name_frame.pack()
        self.name_frame.configure(bg="#ffe8e8")

        # Label 
        self.name_label = Label(self.name_frame, text="Your Name:")
        self.name_label.pack(side=LEFT)
        self.name_label.configure(bg="#ffe8e8")

    def add_name_entry(self):
        # Frame
        self.name_entry = Entry(self.name_frame, width=40)
        self.name_entry.pack(side=RIGHT)

    def add_height_label(self):

        # Frame
        self.height_frame = Frame(pady=10)
        self.height_frame.pack()
        self.height_frame.configure(bg="#ffe8e8")

        # Label 
        self.height_label = Label(self.height_frame, text="Your Height:")
        self.height_label.pack(side=LEFT)
        self.height_label.configure(bg="#ffe8e8")
                

    def add_height_entry(self):
        # Frame
        self.height_entry = Entry(self.height_frame, width=40)
        self.height_entry.pack(side=RIGHT)

    def add_weight_label(self):

        # Frame
        self.weight_frame = Frame()
        self.weight_frame.pack()
        self.weight_frame.configure(bg="#ffe8e8")
        # Label 
        self.weight_label = Label(self.weight_frame, text="Your Weight:")
        self.weight_label.pack(side=LEFT)
        self.weight_label.configure(bg="#ffe8e8")

    def add_weight_entry(self):
        # Frame
        self.weight_entry = Entry(self.weight_frame, width=40)
        self.weight_entry.pack(side=RIGHT)

    def add_buttons(self):
        # Frame
        self.button_frame = Frame()
        self.button_frame.pack(pady=10)

        # Clear Button
        self.clr_button = Button(self.button_frame, text="Clear")
        self.clr_button.pack(side=LEFT)

        # Submission Button
        self.submit_button = Button(self.button_frame, text="Submit")
        self.submit_button.pack(side=RIGHT)

        # Binding 
        self.submit_button.bind("<Button-1>", self.submit_button_click)

    def add_text_block(self):
        self.text_block_frame = Frame()
        self.text_block_frame.pack()
        self.text_block_frame.configure(pady=10, bg="#ffe8e8")

        # Text Block
        self.text_block = Label(self.text_block_frame, text="System Message Displayed Here")
        self.text_block.pack()

        self.text_block.configure(pady=10, height=1, width=50, bg="#fffbce", fg="red")
       
    # Events

    def submit_button_click(self,event):
        self.text_block.configure(text="Calculating...") 

gui = BMI() 
gui.mainloop()