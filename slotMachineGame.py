import random
import os
from enum import Enum


class SlotMachine:
    INITIAL_STAKE = 50
    INITIAL_JACKPOT = 1000

    class Reel(Enum):
        CHERRY = 1
        LEMON = 2
        ORANGE = 3
        PLUM = 4
        BELL = 5
        BAR = 6
        SEVEN = 7

    _values = list(Reel)
    payout = {
        Reel.CHERRY: 7,
        Reel.ORANGE: 10,
        Reel.PLUM: 14,
        Reel.BELL: 20,
        Reel.BAR: 250,
        Reel.SEVEN: 'jackpot'
    }

    def __init__(self, stake = INITIAL_STAKE, jackpot=INITIAL_JACKPOT):
        self.current_stake = stake
        self.current_jackpot = jackpot

    @property
    def keep_playing(self):
        while(True):
            os.system('cls' if os.name == 'nt' else 'clear')
            if self.current_jackpot <= 1:
                print("Machine balance reset.")
                self.current_jackpot = SlotMachine.INITIAL_JACKPOT

            print("The Jackpot is currently: ${}.".format(self.current_jackpot))
            answer = input("Would you like to play? Or check your money? ").lower()
            if answer in ["yes", "y"]:
                return True
            elif answer in ["no", "n"]:
                print("You ended the game with ${} in your hand. Good Game!".format(self.current_stake))
                return False
            elif answer == "check":
                print("You currently have ${}.".format(self.current_stake))
            else:
                print("Couldn't process what you were doing there. Please try again!")

    def _play_round(self):
        first, second, third = random.choice(SlotMachine._values), random.choice(SlotMachine._values), random.choice(SlotMachine._values)
        self._adjust_score(first, second, third)

    def _adjust_score(self, first, second, third):
        if first == SlotMachine.Reel.CHERRY:
            if second == SlotMachine.Reel.CHERRY:
                win = 7 if third == SlotMachine.Reel.CHERRY else 5
            else:
                win = 2
        else:
            if first == second == third:
                win = SlotMachine.payout[first]
                win = self.current_jackpot if win == 'jackpot' else win
            else:
                win = -1

        if win == self.current_jackpot:
            print("YOU WIN THE JACKPOT!!!")
        else:
            print('\t'.join(map(lambda x: x.name.center(6), (first, second, third))))
            print("You {} ${}".format("won" if win > 0 else "lost", win))
            self.current_stake += win
            self.current_jackpot -= win

    def play(self):
        while self.current_stake and self.keep_playing:
            self._play_round()


if __name__ == '__main__':
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
    SlotMachine().play()