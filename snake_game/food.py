from turtle import Turtle
import random

# Food class inherits from Turtle class, so now we have access to all Turtle functions
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('DeepPink')
        self.speed('fastest')
        self.refresh() # This is needed to create the initial food when game starts

    def refresh(self):
        # Create random x and y coordinates within 600x600
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)