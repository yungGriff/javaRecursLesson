import random

thePCnumber = random.randrange(0,10)
counter = 1
exitMsg = "Goodbye."

while True:
    keepPlaying = input("Would you like to play the number guessing game? [Y/N] ").upper()
    if keepPlaying == "Y":
        usersguess = int(input("Guess what number between 0 and 10 I am thinking of! "))
        if thePCnumber > usersguess:
            print("Too low")
            counter += counter
            pass
        elif thePCnumber < usersguess:
            print("Too high")
            counter += counter
            pass
        else:
            print("You got it!!!")
            print("You guessed correctly in: " + str(counter) + " attempt(s)!")
            break
    elif keepPlaying == "EXIT" or keepPlaying == "QUIT":
        print(exitMsg)
        break
    else:
        print(exitMsg)
        break
