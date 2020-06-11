'''Author: Shoaib Adnan
Project name: slotMachineGame
Due date: June 17th
Instructor: Eric Stock'''



import random
import os
import time

print()
print('''Welcome to the python Slot Machine!
You will start with $50 and you will be asked if you want to play.
You can answer with yes/no or you can also use y/n
The chart for winnings for individual combinations are as follows: 
BAR\tBAR\tBAR\t\tpays\t$250
BELL\tBELL\tBELL/BAR\tpays\t$20
PLUM\tPLUM\tPLUM/BAR\tpays\t$14
ORANGE\tORANGE\tORANGE/BAR\tpays\t$10
CHERRY\tCHERRY\tCHERRY\t\tpays\t$7
CHERRY\tCHERRY\t  -\t\tpays\t$5
CHERRY\t  -\t  -\t\tpays\t$2
7\t  7\t  7\t\tpays\tTHE JACKPOT!
''')



def askPlayer():
    ''' Player is asked if he wants to play again '''
    global stake
    global balance
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (balance <=1):
            print ("Slot Machine balance is reset.")
            balance = 1000

        print ("The Jackpot is currently: $" + str(balance) + ".")
        answer = input("Would you like to play (y)? Or check your money? (check)")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(stake) + " in your hand. Excellent job!")
            time.sleep(5)
            return False
        elif(answer == "check" or answer == "CHECK"):
            print ("You currently have $" + str(stake) + ". Keep it going!")
        else:
            print("Couldn't process what you were doing there. Please try again!")