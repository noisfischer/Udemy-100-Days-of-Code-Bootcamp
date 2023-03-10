from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.points = -1
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.update()

    def update(self):
        self.clear()
        self.points += 1
        self.write(f"Score: {self.points}  High Score: {self.high_score}", False, "center", font=("bungee", 20, "normal"))


    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.points = -1
        self.update()

