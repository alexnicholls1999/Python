from tkinter import *
from tkinter import messagebox
import os

DIRNAME, FILENAME = os.path.split(os.path.abspath(__file__))

class Currency(Tk): 
    def __init__(self):
        Tk.__init__(self)
       
        # Style for Window
        self.configure(bg="#ffe8e8")
       
        
        # Add Components 
        self.add_header_label()
        self.add_amount_label()
        self.add_amount_entry()
        self.add_buttons()
        self.add_text_block()

    def add_header_label(self):

        # Label Add 
        self.header_label = Label(text="Currency Converter")
        self.header_label.pack(fill=X)

        # styling 
        self.header_label.configure(font="Arial 18", padx=50, pady=10, bg="#ffe8e8")

    def add_amount_label(self):

        # Label Add 
        self.amount_label = Label(text="Amount")
        self.amount_label.pack(anchor=W)

        # styling 
        self.amount_label.configure(font="Arial 10", padx=10, pady=10, bg="#ffe8e8")
        
    def add_amount_entry(self):

        self.amount_frame = Frame()
        self.amount_frame.pack()
        self.amount_frame.configure(bg="#ffe8e8")

        # Label Add 
        self.amount_entry = Entry(self.amount_frame, width=40)
        self.amount_entry.pack(side=LEFT)
        self.amount_entry.bind("<KeyRelease>")
        
        self.wrong = PhotoImage(file=DIRNAME + "\\wrong.png")
        self.wrong = self.wrong.subsample(20,20)

        self.right = PhotoImage(file=DIRNAME + "\\right.png")
        self.right = self.right.subsample(20,20)
        
        self.validation = Label(self.amount_frame,image=self.wrong)
        self.validation.pack(side=RIGHT, padx=10)


        if (self.amount_entry.get() != ""):
            self.validation.configure(image=self.right)
        else:
            self.validation.configure(image=self.wrong)
            
        
    def add_buttons(self):

        # frame
        self.btn_frame = Frame()
        self.btn_frame.pack()
    
        # styling frame
        self.btn_frame.configure(bg="#ffe8e8")

        # convert button 
        self.btn_convert = Button(self.btn_frame, text="Convert")
        self.btn_convert.pack(side=RIGHT)

        # style convert button 
        self.btn_convert.configure(bg="#ffe8e8")

        # Bind 
        self.btn_convert.bind("<Button-1>", self.convert_button_click)

        # clear button 
        self.btn_clr = Button(self.btn_frame, text="Clear")
        self.btn_clr.pack(side=LEFT)     

        # event clear
        self.btn_clr.bind("<Button-1>", self.clear_button_click)

    def add_text_block(self):

        # Text Block
        self.txt_block = Label(text='System Message Display Here')
        self.txt_block.pack() 

        # Styling 
        self.txt_block.configure(pady=10, height=10, width=50, bg="#fffbce")

    # Event Functions

    def clear_button_click(self, event):

        self.amount_entry.delete(0, END)
        self.txt_block.configure(text="System Message Display Here")
    
    def convert_button_click(self, event):
        
        self.btn_clr.bind("<Button-1>", self.clear_button_click)
        self.txt_block.configure(text="Converting..")

    

gui = Currency()
gui.mainloop()