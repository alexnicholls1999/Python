from tkinter import *

# Class which desbcribes what the gui looks like and behaves like
class Cacti(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Display default image
        self.cacti_image = PhotoImage(file="C:/Users/azini/Documents/python/cacti.gif", width=220, height=220)
        self.cacti_label = Label(image=self.cacti_image)
        self.cacti_btn = Button (text="Flip Button")

        # Grid
        self.cacti_label.grid(row=1, column= 1)
        self.cacti_btn.grid(row= 2, column= 1, pady= 1)

        # Bind
        self.cacti_btn.bind("<Button-1>", self.test_button_1_clicked) 
        self.cacti_btn.bind("<Button-3>", self.test_button_3_clicked )
    
    def test_button_1_clicked(self, Button):
        self.cacti_image2 = PhotoImage(file="C:/Users/azini/Documents/python/cact2.gif", width=220, height=220)
        self.cacti_label.configure(image = self.cacti_image2)
    
    def test_button_3_clicked(self, Button):
        self.cacti_image = PhotoImage(file="C:/Users/azini/Documents/python/cacti.gif", width=220, height=220)
        self.cacti_label.configure(image = self.cacti_image)

# the object - GUI itself
gui = Cacti()
gui.mainloop()