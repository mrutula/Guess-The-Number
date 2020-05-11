import random
import sys
import pyinputplus as pyip

class GuessTheNumber:  
    """
    This is a class to compare user's guess with the randomly generated number
    
    Attributes:
        guess (int): User's guess
    """ 
    def __init__(self, guess):
        self.guess = guess
    
    def randomgenerator(self):
        """
        The function to generate a random number between 1 and 20

        Return:
            number: random number generated
        """
        number = random.randint(1, 20)
        return number
    
    def isguessright(self):
        """The function to check if user guess is right"""
        number = self.randomgenerator()
        if self.guess < number:
            print(f"Your guess {self.guess} is too low")
        elif self.guess > number:
            print(f"Your guess {self.guess} is too high")
        else:
            print(f"You guessed it right!!!!")

if __name__ == '__main__':
    while True:
        user_choice = pyip.inputChoice(['play','quit'])    
        if user_choice == 'play':
            user_input = pyip.inputNum("Enter a number between 1 and 20\t", min=1, max=20)
            guess = GuessTheNumber(user_input)
            guess.isguessright()
        elif user_choice == 'quit':
            break
        







