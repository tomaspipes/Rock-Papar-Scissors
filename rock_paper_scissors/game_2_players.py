from getpass import getpass
from person import Person

class Game_2_Players:

    def __init__(self):
        self.person = Person()
        self.person2 = Person()
        self.person.get_name_person_1()
        self.person2.get_name_person_2()
        self.person.read_line1()
        self.person2.read_line2()
        self.person_points = 0
        self.person2_points = 0
        self.rounds = 0      
        self.start_game()

    def person_wins(self):
        self.person_points += 1
        print("Congratulations "+ self.person.firstLine +", you've won this round\n" + self.person.firstLine + " points: " + str(self.person_points) + " || " +self.person2.firstLine_2 + " points: " + str(self.person2_points))
    
    def person2_wins(self):
        self.person2_points += 1
        print("Congratulations "+ self.person2.firstLine_2 +", you've won this round\n" + self.person.firstLine + " points: " + str(self.person_points) + " || " +self.person2.firstLine_2 + " points: " + str(self.person2_points))
    
    def same_option(self):
        print("You chose the same option\n")

    def start_game(self):

        options = ["rock", "paper", "scissors"]
        max_score = int(input("Enter the max_score = "))

        while self.rounds < max_score:
            user_opt = getpass(self.person.firstLine + " insert your option: ")
            user_opt2 = getpass(self.person2.firstLine_2 + " insert your option: ")
            print (self.person.firstLine + " choose: "+ user_opt)
            print (self.person2.firstLine_2 + " choose: " + user_opt2)


            userRockOption = user_opt.startswith(options[0][0].upper()) or user_opt.startswith(options[0][0].lower()) ## True or False
            userPaperOption = user_opt.startswith(options[1][0].upper()) or user_opt.startswith(options[1][0].lower()) ## True or False
            userScissorsOption = user_opt.startswith(options[2][0].upper()) or user_opt.startswith(options[2][0].lower()) ## True or False

            user2_RockOption = user_opt2.startswith(options[0][0].upper()) or user_opt2.startswith(options[0][0].lower()) ## True or False
            user2_PaperOption = user_opt2.startswith(options[1][0].upper()) or user_opt2.startswith(options[1][0].lower()) ## True or False
            user2_ScissorsOption = user_opt2.startswith(options[2][0].upper()) or user_opt2.startswith(options[2][0].lower()) ## True or False

            if userRockOption and user2_ScissorsOption:
                    
                self.person_wins()

            elif  userRockOption and user2_PaperOption:

                self.person2_wins()

            elif userRockOption and user2_RockOption:

                self.same_option()

            elif userPaperOption and user2_RockOption:
                    
                self.person_wins()

            elif userPaperOption and user2_ScissorsOption:
                    
                self.person2_wins()

            elif userPaperOption and user2_PaperOption:
                    
                self.same_option()

            elif userScissorsOption and user2_PaperOption:
                    
                self.person_wins()

            elif userScissorsOption and user2_RockOption:
                    
                self.person2_wins()

            elif userScissorsOption and user2_ScissorsOption:
                    
                self.same_option()
            
            self.rounds += 1

        if self.person_points > self.person2_points:

            print(self.person.firstLine + " wins")

        elif self.person_points < self.person2_points:

            print(self.person2.firstLine_2 + " wins")

        else:
            print("You drew")