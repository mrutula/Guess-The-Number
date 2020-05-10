import random
import sys

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
        user_input = input("Enter a number between 1 and 20\t")
        if user_input == 'quit':
            break
        try:
            user_num = int(user_input)
            guess = GuessTheNumber(int(user_num))
            guess.isguessright()
        except ValueError:
            print(f"This is not a valid number. It isnt a number at all! This is a string, go and try again, Better luck next time")









