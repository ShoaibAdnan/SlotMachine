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

time.sleep(10)

INIT_STAKE = 50
INIT_BALANCE = 1000
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "7"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE
balance = INIT_BALANCE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    while(stake != 0 and playQuestion == True):
        firstWheel = spinWheel()       
        secondWheel = spinWheel()
        thirdWheel = spinWheel()
        printScore()               
        playQuestion = askPlayer()

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
        answer = input("Would you like to play (y)? Or check your money? (check): ")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("You ended the game with $" + str(stake) + " in your hand. Good Game!")
            time.sleep(5)
            return False
        elif(answer == "check" or answer == "CHECK"):
            print ("You currently have $" + str(stake) + ". Keep it going!")
        else:
            print("Couldn't process what you were doing there. Please try again!")
            
def spinWheel():
    ''' returns a random item from the wheel '''
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore():
    ''' prints the current score '''
    
    global stake, firstWheel, secondWheel, thirdWheel, balance
    
    if((firstWheel == "CHERRY") and (secondWheel != "CHERRY")):
        win = 2
        balance -= 2
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel != "CHERRY")):
        win = 5
        balance -= 5
    elif((firstWheel == "CHERRY") and (secondWheel == "CHERRY") and (thirdWheel == "CHERRY")):
        win = 7
        balance -= 7
    elif((firstWheel == "ORANGE") and (secondWheel == "ORANGE") and ((thirdWheel == "ORANGE") or (thirdWheel == "BAR"))):
        win = 10
        balance -= 10
    elif((firstWheel == "PLUM") and (secondWheel == "PLUM") and ((thirdWheel == "PLUM") or (thirdWheel == "BAR"))):
        win = 14
        balance -= 14
    elif((firstWheel == "BELL") and (secondWheel == "BELL") and ((thirdWheel == "BELL") or (thirdWheel == "BAR"))):
        win = 20
        balance -= 20
    elif((firstWheel == "BAR") and (secondWheel == "BAR") and (thirdWheel == "BAR")):
        win = 250
        balance -= 250
    elif((firstWheel == "7") and (secondWheel == "7") and (thirdWheel == "7")):
        win = balance
        balance -= win
    else:
        win -= 1
        balance += 1

    stake += win
    
    if win == balance:
        print ("YOU WIN THE JACKPOT!!!")
        
    if(win > 0):
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You win $' + str(win))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(firstWheel + '\t' + secondWheel + '\t' + thirdWheel + ' -- You lose')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

play()