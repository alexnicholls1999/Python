#lotto
def main():
    from random import shuffle

    print("Welcome to Lotto Number Generator!")
    input("Press [Enter] to start the generator..")

    lotto = list(range(1,60))
    lucky = list(range(1,60))
    numbers = []
    bonus = []

    for i in range(5):
        shuffle(lotto)
        x = lotto.pop()
        numbers.append(x)

    for i in range(1):
        shuffle(lucky)
        x = lucky.pop()
        bonus.append(x)   

    print ("Your five numbers are: ", numbers)
    print ("And your lucky bonus number is", bonus)

    restart = input("Would you like new numbers?" )
    if restart == "yes":
        main()
    else: 
        exit()
main()