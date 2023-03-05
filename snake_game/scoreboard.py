from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.update()


    points = -1
    def update(self):
        self.clear()
        self.points += 1
        self.write(f"Score: {self.points}", False, "center", font=("bungee", 20, "normal"))


    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", font=("bungee", 64, "normal"))
