from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)  # Stops anything from appearing on screen

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
# For arrow keys, we have made predefined functions for turning in our Snake class
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    # Skips animations and only updates the screen when the action has happened
    screen.update()
    # Every 0.1 seconds the screen will update
    time.sleep(0.07)
    # Snake will move forwards according to our function we made in the Snake class
    snake.move()
    # Detect collision with food. The food is a 10x10 circle
    if snake.head.distance(food) < 15:
        food.refresh() # Food is eaten and spawns randomly elsewhere
        scoreboard.update() # Score increases by 1
        snake.extend()  # Snake tail increases by 1 square

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail. The [1:] starts from the second index so the head doesn't collide with itself
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

























screen.exitonclick()