from tkinter import *



root = Tk()

root.title("Currency Converter")

class Sum: 
    def _init_(self)
        

    def clear(self):
        e1.delete(0,END)

# Converter Function
    def conversion(self)


s = Sum()

l1 = Label(root, text="Currency Converter", font=("Arial", 20)).grid(row=0, columnspan=6, sticky='N')
l2 = Label(root, text="Amount").grid(row=1, column=1, padx=10, sticky='W')

e1 = Entry(root, width=80).grid(row=2, column=1, columnspan=5, padx=10, sticky='W')
e2 = Entry(root, width=80).grid(row=4, column=1, columnspan=5, pady=30)

b1 = Button(root, width= 10, text="Clear", command=s.clear).grid(row=3, column=2, columnspan=1, padx=50, pady=10, sticky='W')
b2 = Button(root, width= 10, text="Convert").grid(row=3, column=2, columnspan=1, sticky='E')


root.mainloop()