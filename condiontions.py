def condiontions(myString):
	print (myString)
	myName = input("What is your name?")
	myVar = input("Enter a number")
	print (myName)


	if (myName == "Kevin" or myVar != 0):
		print("Kevin is great!")
	elif(myName == "Bob"):
		print("Bob is Okay")
	else: 
		print("Hello World")

condiontions("Hello User")
condiontions("Numbers")
