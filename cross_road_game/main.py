from turtle import Screen
from player import Player
from level import Level
from cars import Cars
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Level()
car = Cars()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
speed = 10
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if cars.distance(player) < 15:
            level.game_over()
            game_is_on = False

    if player.ycor() > 270:
        level.update()
        player.restart()
        car.speed_up(speed)
        speed += 5

    if level.num_level > 10:
        level.winner_message()
        game_is_on = False


screen.exitonclick()