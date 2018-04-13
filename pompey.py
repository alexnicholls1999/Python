wrong_parameters = True

def start (): 
	print ("Pompey odds on winning League One")

	portsmouth_win_the_league = str(input())
	

	if portsmouth_win_the_league == "Yes": 
			wrong_parameters = False
			print ("We Are Going Up oh We Are Going Up")
			
			
	elif portsmouth_win_the_league == "No": 
			wrong_parameters = False x 
			print ("Shit Season")
			
	else: 
		print("You have not enter the right parameters!")
		print("Try Again!")

while wrong_parameters : 
	start()

