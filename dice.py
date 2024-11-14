import random
import threading
''' D6: Dice with 6 Sides
    1. Random Number Gennerators
        - Needs to be on a timed basis how fast do dice roll
            > The amount of rolling decreases as the dice looses energy due to friction
            > The time that dice roll is diffrent so the numbers should gennerate random for diffrent durations of time. 
        - Needs to show what number it is on
    2. Saves to Mongo DB
    3. Gets implemented into the graph
'''
""" I want to use the threading module to make it slow down over time
    The dice will have numbers on the screen that will at first be fast but then be slower and slower until it lands on the final random number.
    """
class dice:
    """ Have """
    def __init__(self, sides = 6, lower_time = 0, upper_time = 10): #Initlizes the programs data
        self.sides = sides
        self.lower_time = lower_time
        self.upper_time = upper_time

    def getSides(self):
        return self.sides
    
    def roll(self):
        random1 = random.randint(0, self.getSides())
        return random1