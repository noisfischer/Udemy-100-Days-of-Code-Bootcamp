import turtle
from turtle import Turtle, Screen
from paddle_1 import Paddle_1
from paddle_2 import Paddle_2
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.title('PONG')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

paddle_1 = Paddle_1()
paddle_2 = Paddle_2()
ball = Ball()
scoreboard_r = Scoreboard(paddle_1)
scoreboard_l = Scoreboard(paddle_2)
final_score_left = Turtle()
final_score_right = Turtle()

list = []
y_cor = 275
for lines in range(10):
    new_line = Turtle(shape='square')
    new_line.color('white')
    new_line.shapesize(1, 0.5)
    new_line.penup()
    new_line.goto(0, y_cor)
    y_cor -= 60
    list.append(new_line)

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

while scoreboard_l.points < 3 and scoreboard_r.points < 3:
    ball.goto(0, 0)
    game_is_on = True
    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        ball.bounce(paddle_1, paddle_2)
        if 390 < ball.xcor() < 400:
            scoreboard_l.update()
            ball.setheading(135)
            game_is_on = False
            ball.move_speed = 0.025
            paddle_1.reset_paddle()
            paddle_1.goto(350, 0)
            paddle_2.reset_paddle()
            paddle_2.goto(-350, 0)

        elif -390 > ball.xcor() > -400:
            scoreboard_r.update()
            ball.setheading(45)
            game_is_on = False
            ball.move_speed = 0.025
            paddle_1.reset_paddle()
            paddle_1.goto(350, 0)
            paddle_2.reset_paddle()
            paddle_2.goto(-350, 0)


if scoreboard_l.points == 3:
    final_score_left.color('green')
    final_score_left.goto(-175, 0)
    final_score_left.write("WINNER", False, "center", font=("bungee", 64, "normal"))
    final_score_right.color('red')
    final_score_right.goto(175, 0)
    final_score_right.write("LOSER", False, "center", font=("bungee", 64, "normal"))

elif scoreboard_r.points == 3:
    final_score_left.color('red')
    final_score_left.goto(-175, 0)
    final_score_left.write("LOSER", False, "center", font=("bungee", 64, "normal"))
    final_score_right.color('green')
    final_score_right.goto(175, 0)
    final_score_right.write("WINNER", False, "center", font=("bungee", 64, "normal"))


screen.exitonclick()