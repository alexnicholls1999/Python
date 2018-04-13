from tkinter import *

# Class which desbcribes what the gui looks like and behaves like
class Bus(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Display default image
        self.map_image = PhotoImage(file="C:/Users/azini/Documents/python/westeros.gif", width=1500, height=1000)
        self.dragon_image = PhotoImage(file="C:/Users/azini/Documents/python/dragon.gif", width=200, height=200)
        self.map_image_label = Label(image=self.map_image)
        self.dragon_label = Label(image=self.dragon_image)

        # Place
        self.dragon_label.place(x = 5, y = 5)
        self.map_image_label.place(x = 5, y = 5)
 

        # Bind
        self.dragon_label.bind("<B1-Motion>",self.motion) 
        
    def motion(self, event):
        self.dragon_label.place(x =event.x, y =event.y)
    

    

   

# the object - GUI itself
gui = Bus()
gui.mainloop()