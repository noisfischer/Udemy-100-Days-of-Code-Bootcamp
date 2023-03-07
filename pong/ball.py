from turtle import Turtle

UP_RIGHT = 45
DOWN_RIGHT = 315
UP_LEFT = 135
DOWN_LEFT = 225

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.setheading(UP_RIGHT)
        self.move_speed = 0.025

    def move(self):
        if self.heading() == UP_RIGHT or self.heading() == DOWN_RIGHT:
            self.forward(10)
        elif self.heading() == UP_LEFT or self.heading() == DOWN_LEFT:
            self.forward(10)

    def bounce(self, paddle_r, paddle_l):
        if self.heading() == UP_RIGHT or self.heading() == DOWN_RIGHT:
            if self.ycor() > 290:
                self.setheading(DOWN_RIGHT)
            elif self.ycor() < -290:
                self.setheading(UP_RIGHT)
            elif self.distance(paddle_r) < 50 and self.xcor() > 340 and self.heading() == UP_RIGHT:
                self.setheading(UP_LEFT)
                self.move_speed -= .0025
            elif self.distance(paddle_r) < 50 and self.xcor() > 340 and self.heading() == DOWN_RIGHT:
                self.setheading(DOWN_LEFT)
                self.move_speed -= .0025

        elif self.heading() == UP_LEFT or self.heading() == DOWN_LEFT:
            if self.ycor() > 290:
                self.setheading(DOWN_LEFT)
            elif self.ycor() < -290:
                self.setheading(UP_LEFT)
            elif self.distance(paddle_l) < 50 and self.xcor() < -340 and self.heading() == UP_LEFT:
                self.setheading(UP_RIGHT)
                self.move_speed -= .0025
            elif self.distance(paddle_l) < 50 and self.xcor() < -340 and self.heading() == DOWN_LEFT:
                self.setheading(DOWN_RIGHT)
                self.move_speed -= .0025

        else:
            self.move()



