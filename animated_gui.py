from tkinter import*
import time

# the class
class AnimatedGui(Tk):
    def __init__(self):
        Tk.__init__(self)

        # set the size of the window
        self.geometry("500x500")

        # track the position of the ball
        self.ball_x_pos = 200
        self.ball_y_pos = 200
        self.ball_x_change = 0
        self.ball_y_change = 0

        # load the image of the ball
        self.ball_image = PhotoImage(file="ball.gif")
        self.ball_label = Label(image=self.ball_image)
        self.ball_label.place(x=self.ball_x_pos, y=self.ball_y_pos)

        # Time
        self.tick()

        # timer tick function
    def tick(self):
        
        # move the ball by the change amount
        self.ball_y_pos = self.ball_y_pos + self.ball_y_change
        self.ball_label.place(x=self.ball_y_pos, y=self.ball_x_pos)

        self.after(100, self.tick)


# the object
if __name__ == "__main__":
    gui = AnimatedGui()
    gui.mainloop()
