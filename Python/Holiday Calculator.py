import tkinter as t

flights,accomondation,foods,activities, miscellaneuos, result = None, None, None, None, None, None


def run():
         global flights,accomondation,foods,activities, miscellaneuos, result

         root = t.Tk()
         
         flights_label = t.Label(root, text="Cost of flights")
         accomondation_label = t.Label(root, text="Cost of accomondation")
         food_label = t.Label(root, text="Cost of food")
         activities_label = t.Label(root, text="Cost of activites")
         miscellaneuous_label = t.Label(root, text="Cost of miscellanous")

         flights = t.Entry(root)
         accomondation = t.Entry(root)
         foods = t.Entry(root)
         activities = t.Entry(root)
         miscellaneuos = t.Entry(root)
         result = t.Entry(root, state="readonly")
                 

         flights_label.grid (row=0, column=1, sticky ='W')
         accomondation_label.grid (row=1, column=1 ,sticky ='W')
         food_label.grid (row=2, column=1 ,sticky ='W')
         activities_label.grid (row=3, column=1 ,sticky ='W')
         miscellaneuous_label.grid (row=4, column=1,sticky ='W')

         flights.grid (row=0, column=2, sticky ='E')
         accomondation.grid (row=1, column=2, sticky ='E')
         foods.grid (row=2, column=2, sticky ='E')
         activities.grid (row=3, column=2, sticky = 'E')
         miscellaneuos.grid (row=4, column=2,sticky = 'E')
         result.grid (row=6, column=2,sticky = 'E')


         t.Button (root, text="Calculate", command=Calculate).grid(row=5, column=2, sticky=t.E)
         

         root.mainloop()

def Calculate():
         try:
             val = sum([int(flights.get()), int(accomondation.get()), int(foods.get()), int(activities.get()), int(miscellaneuos.get())])
         except Exception as e:
             val = e
         result.configure(state=t.NORMAL)
         result.delete(0, t.END)
         result.insert(0, val)
         result.configure(state=t.DISABLED)



run() 
         
