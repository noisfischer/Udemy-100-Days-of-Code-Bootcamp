from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.goto(0, -270)

    def move(self):
        self.forward(20)

    def restart(self):
        self.goto(0, -270)