import random
# r > s 
# s > p
# p > r  
def randomThrow():
    # x = random.randrange(0,2)
    number = random.randint(0,2)
    if number == 0:
       return "r" 
    elif number == 1:
       return "s"
    elif number == 2:
       return "p"
    else:
        print("out-of-bounds")

# def throw(hand):



while True:
    keepPlaying = input("Would you like to play roshambo?  [Y/N] ").upper()
    if keepPlaying == "Y":
        throw = input("Please decide what you want to play: r-Rock, s-Shears, p-Paper ")
        pcthrow = randomThrow()
        if throw == "r":
            if pcthrow == "p":
                print("You lost!")
            elif pcthrow == "s":
                print("You won!")
            else: 
                print("Tied!")
        if throw == "s":
            if pcthrow == "r":
                print("You lost!")
            elif pcthrow == "p":
                print("You won!")
            else:
                print("Tied!")
        if throw == "p":
            if pcthrow == "s":
                print("You lost!")
            elif pcthrow == "r":
                print("You won!")
            else:
                print("Tied!")
    elif keepPlaying == "N":
        print("Goodbye")
        break
    else: 
        continue

