from tkinter import *
from tkinter import messagebox
import os 
import re

DIRNAME, FILENAME = os.path.split(os.path.abspath(__file__))

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
        self.name_entry.bind("<KeyRelease>", self.validation)
    

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

        # Validation Height
        self.height_entry.bind("<KeyRelease>", self.validation)

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

        self.weight_entry.bind("<KeyRelease>", self.validation)

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
        self.submit_button.bind("<ButtonRelease-1>", self.submit_button_click)
        self.clr_button.bind("<Button-1>", self.clr_button_click)

    def add_text_block(self):
        self.text_block_frame = Frame()
        self.text_block_frame.pack()
        self.text_block_frame.configure(pady=10, bg="#ffe8e8")

        # Text Block
        self.text_block = Label(self.text_block_frame, text="System Message Displayed Here")
        self.text_block.pack()

        self.text_block.configure(pady=10, height=1, width=50, bg="#fffbce", fg="red")
       
    # Events

    def submit_button_click(self, event):
        self.text_block.configure(text="Calculating...") 
        
        weight = int(self.weight_entry.get())
        height = int(self.height_entry.get())

        BMI = weight/(height * height)

        message = 'The BMI for a weight of %s and a height of %s. BMI %s' %(weight,height,BMI)      
        

        messagebox.showinfo("BMI", message)
    
    def clr_button_click(self, event):

        self.name_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.weight_entry.delete(0, END)

        self.text_block.configure(text="System Message Displayed Here")    
    
    def validation(self, event):
        self.wrong = PhotoImage(file=DIRNAME + "\\wrong.png")
        self.wrong = self.wrong.subsample(20,20)

        self.right = PhotoImage(file=DIRNAME + "\\right.png")
        self.right = self.right.subsample(20,20)

        self.validation_name = Label(self.name_frame,image=self.wrong)
        self.validation_name.pack(side=RIGHT)

        self.validation_height = Label(self.height_frame, image=self.wrong)
        self.validation_height.pack(side=RIGHT)

        self.validation_weight = Label(self.weight_frame, image=self.wrong)
        self.validation_weight.pack(side=RIGHT)

       
        # Name Validation If statement
        if (self.name_entry.get() != ""):
            self.validation_name.configure(image=self.right)
        else:
            self.validation_name.configure(image=self.wrong)
        
        # Height Validation If statement
        if (self.height_entry.get() != ""):
            self.validation_height.configure(image=self.right)
        else: 
            self.validation_height.configure(image=self.wrong)

        # Weight Validation If statement
        if (self.weight_entry.get() != ""):
            self.validation_weight.configure(image=self.right)            
        else: 
            self.validation_weight.configure(image=self.wrong)


gui = BMI() 
gui.mainloop()        