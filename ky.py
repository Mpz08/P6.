# Lab 8
# Name:
# Date:
# Description: Plays rock, paper, scissors with the user, except replaces the weapons with superheroes from Marvel
# Rules:
# (1) Thor beats Captain America because Captain America has no defense against lightning
# (2) Iron Man beats Thor because Iron Man absorbs the lightning
# (3) Captain America beats Iron Man because Captain America always has the moral high ground over Iron Man

print ("Welcom and it's time to play AVENGERS: CIVIL WAR!")

# C = 'Captain America'
# I = 'Iron Man'
# T = 'Thor'

import random

character = ["C","I","T"]
random.randint(0,3)


while True:
    player = input("  Choose a character: (C)aptain America, (I)ron Man, or (T)hor:\n ")
    if player in character:
        oppent = random.choice(character)
        print = (f"you have choosen {player}, the oppent has choosen {oppent}.\n ")
        if player == oppent:
            print = (f"you and your oppent has choosen {player}. It is a tie\n ")
        elif player == "C":
            if oppent == "I":
                print ("Captain America beats Iron Man because Captain America always has the moral high ground over Iron Man")
                print("The challenger is victories")
        elif player == "I":
            if oppent == "T":
                print ("Iron Man beats Thor because Iron Man absorbs the lightning")
                print("The challenger is victories")
        elif player == "T":
            if oppent == "C":
                print ("Thor beats Captain America because Captain America has no defense against lightning")
                print("The challenger is victories")

        elif player == "I":
            if oppent == "C":
                print ("Captain America beats Iron Man because Captain America always has the moral high ground over Iron Man")
                print("The challenger is has not returned victories today")
        elif player == "T":
            if oppent == "I":
                print ("Iron Man beats Thor because Iron Man absorbs the lightning")
                print("The challenger is has not returned victories today")
        elif player == "C":
            if oppent == "T":
                print ("Thor beats Captain America because Captain America has no defense against lightning")
                print("The challenger is has not returned victories today")

    else:
        print = (f"Sorry what is '{character}'?, Is was a typ o. OK!\n ")
    play_again = ("Take a onther shote? (y/n) \n : ")
    if play_again.lower() == "n":
        break

        print()

print("\nCan not handl the heat")


