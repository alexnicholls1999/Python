
print ("Welcome to the Planet Of The Apes...")



countapes = 0
counthuman = 0

print ("...be human or be ye ape?")

name = str(input())

if (name == "Human" or "human"):
	counthuman += 1
	print ("I did not start this war. But I will finish it.")
elif (name == "Ape"): 
	countapes += 1
	print ("Apes together strong")
else:
	print ("This is not your fight.")

print ("Total of apes", countapes)
print ("Total of humans", counthuman)

		
