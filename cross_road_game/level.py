from turtle import Turtle


class Level(Turtle):

    num_level = 1

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(-220, 270)
        self.hideturtle()
        self.write(f"Level: {self.num_level}", False, "center", ("bungee", 24, "normal"))

    def update(self):
        self.clear()
        self.num_level += 1
        if self.num_level > 10:
            self.write(f"Level: 10", False, "center", ("bungee", 24, "normal"))
        else:
            self.write(f"Level: {self.num_level}", False, "center", ("bungee", 24, "normal"))

    def game_over(self):
        self.end_message = Turtle()
        self.end_message.penup()
        self.end_message.color('red')
        self.end_message.goto(0, 0)
        self.end_message.write("GAME OVER", False, "center", ("bungee", 64, "normal"))

    def winner_message(self):
        self.win_message = Turtle()
        self.win_message.penup()
        self.win_message.color('green')
        self.win_message.goto(0, 0)
        self.win_message.write("YOU WIN!", False, "center", ("bungee", 64, "normal"))
