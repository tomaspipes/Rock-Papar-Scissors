from game import Game
import sys
from instructions import Instructions
from game_2_players import Game_2_Players

class Type_Of_Game:
    
    def __init__(self):
        self.option_choosed = input ("Press: 1 --> VS Computer || 2 --> Multiplayer || I --> Instructions || Q --> Quit ")
        self.starting_game()


    def starting_game(self):

        if self.option_choosed == '1':
            g = Game()
        elif self.option_choosed == "quit" or self.option_choosed == "q":
            sys.exit()
        elif self.option_choosed == "I" or self.option_choosed == "i":
            i = Instructions()
        elif self.option_choosed =='2':
            z = Game_2_Players()  
        else:
            print ('Wrong input, choose a valid one.')

    