class Person:

    def get_name_person_1(self):
        self.name = input("Player1 name: ")

    def get_name_person_2(self):
        self.name2 = input("Player2 name: ")


    def read_line1(self):
        
        if self.name != '':

            with open("name.txt", "w") as f:
                f.writelines(self.name)

        varia = open('name.txt', 'r')
        self.firstLine = varia.readline()
        

    def read_line2(self):
        
        if self.name2 != '':

            with open("name_2.txt", "w") as f:
                f.writelines(self.name2)

        varia_2 = open('name_2.txt', 'r')
        self.firstLine_2 = varia_2.readline()

