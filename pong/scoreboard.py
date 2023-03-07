from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, paddle):
        super().__init__()
        if paddle.xcor() > 0:
            self.penup()
            self.hideturtle()
            self.goto(100, 220)
            self.color('white')
            self.update()
        else:
            self.penup()
            self.hideturtle()
            self.goto(-100, 220)
            self.color('white')
            self.update()

    points = -1
    def update(self):
        self.clear()
        self.points += 1
        self.write(f"{self.points}", False, "center", font=("bungee", 64, "normal"))
