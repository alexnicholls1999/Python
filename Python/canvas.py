from tkinter import * 

# the class (blue print)
class CanvasGui(Tk):

    def __init__(self):
        Tk.__init__(self)

        # canvas
        self.canvas = Canvas(width=500, height=500)
        self.canvas.pack()

        # line
        self.canvas.create_line(50, 250, 450, 250)
        self.canvas.create_line(50, 250, 50, 500)
        self.canvas.create_line(450, 50, 500, 50)

gui = CanvasGui()
gui.mainloop()

