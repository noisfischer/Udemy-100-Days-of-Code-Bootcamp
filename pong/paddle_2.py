from turtle import Turtle


class Paddle_2(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.turtlesize(5, 1)
        self.goto(-350, 0)

    new_y = 0

    def up(self):
        if self.ycor() < 240:
            self.new_y += 40
            self.goto(-350, self.new_y)

    def down(self):
        if self.ycor() > -240:
            self.new_y -= 40
            self.goto(-350, self.new_y)

    def reset_paddle(self):
        self.new_y = 0

