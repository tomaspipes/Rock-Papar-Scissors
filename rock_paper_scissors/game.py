from person import Person

import random
import time
from instructions import Instructions


class Game:

    def __init__(self):
        self.person = Person()
        self.person.get_name_person_1()
        self.person.read_line1()
        self.person_points = 0
        self.computer_points = 0
        self.rounds = 0
        self.start_game()

    def person_wins(self):
        self.person_points += 1
        print("\n" + self.person.firstLine + " points: " + str(self.person_points) + " || Computer points: " + str(self.computer_points))

    def computer_wins(self):
        self.computer_points += 1
        print("\n" + self.person.firstLine + " points: " + str(self.person_points) + " || Computer points: " + str(self.computer_points))

    def same_option(self):
        print("\n" + self.person.firstLine + " points: " + str(self.person_points) + " || Computer points: " + str(self.computer_points))
             

    def start_game(self):
        
        
        options = ["Rock", "Paper", "Scissors"]
        max_score = int(input("Enter the max_score = "))
                    

        while self.rounds < max_score:
            
            user_opt = input("Insert your option: ")

            computer_opt = random.choice(options)

            print("Computer chose: " + computer_opt)

            userRockOption = user_opt.startswith(options[0][0].upper()) or user_opt.startswith(options[0][0].lower()) ## True or False
            userPaperOption = user_opt.startswith(options[1][0].upper()) or user_opt.startswith(options[1][0].lower()) ## True or False
            userScissorsOption = user_opt.startswith(options[2][0].upper()) or user_opt.startswith(options[2][0].lower()) ## True or False

            computerScissorsOption = computer_opt == options[2] ## True or False
            computerPaperOption = computer_opt == options[1]
            computerRockOption = computer_opt == options[0]

            
            if userRockOption and computerScissorsOption:
                self.person_wins()

            elif  userRockOption and computerPaperOption:
                self.computer_wins()

            elif userRockOption and computerRockOption:
                self.same_option()

            elif userPaperOption and computerRockOption:                   
                self.person_wins()

            elif userPaperOption and computerScissorsOption:
                self.computer_wins()

            elif userPaperOption and computerPaperOption:
                self.same_option()

            elif userScissorsOption and computerPaperOption:
                self.person_wins()

            elif userScissorsOption and computerRockOption:
                self.computer_wins()

            elif userScissorsOption and computerScissorsOption:
                self.same_option()
            
            self.rounds += 1
        

        if self.person_points > self.computer_points:

            print(self.person.firstLine + " wins with " + str(self.person_points) + " points")

        elif self.person_points < self.computer_points:

            print("Computer wins with " + str(self.computer_points) + " points")

        else:
            print("You drew")
    

            