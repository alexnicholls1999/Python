from tkinter import *

#classes
class AlexsButtons:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=master.destroy)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this actually worked!")
        


#event mouse clicks
#def printName(event):
#    print("Hello my name is Alf")
#button_1 = Button(root, text="Print my name",) #command=printName 
#button_1.bind("<Button-1>", printName())
#button_1.pack()

#def leftClick(event):
#    print("Left")
#def middleClick(event):
#    print("Middle")
#def rightClick(event):
#    print("Right")

#frame = Frame(root, width=300, height=250)
#frame.bind("<Button-1>", leftClick)
#frame.bind("<Button-2>", middleClick)
#frame.bind("<Button-3>", rightClick)
#frame.pack()



root = Tk()        
a = AlexsButtons(root)
root.mainloop()
