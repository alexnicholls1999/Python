#User Enters weight in Kilograms
print ("What is your weight? (kg)?")
weight = int(input())

#User Enters Height in Metres 
print ("What is your height? (m)")
height = float(input())

#Users BMI 
print ("Your bmi is","{0:.2f}".format(weight/height**2))