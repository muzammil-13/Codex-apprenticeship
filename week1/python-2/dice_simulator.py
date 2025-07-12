import random

# define a dice class to represent a dice object
class Dice:
    def __init__(self,sides=6):
        # initialize the dice with a number of slides (default is 6)
        self.sides=sides

    def roll(self):
        # return a random number between 1 and the number of sides
        return random.randit(1,self.sides)

# main program to use the dice class
if __name__=="main":
    # create a standard 6-sided dice
    dice=Dice()
    print("Dice simulator")
    while True:
        user_input=input("Press enter to roll the dice (or type 'q' to quit): ")
        if user_input.lower()=='q':
            print("Existing Dice simulator")
            break

        result=dice.roll()
        print(f"You rolled a {result}!")
    