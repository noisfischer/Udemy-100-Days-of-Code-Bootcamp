import colorgram
from turtle import Turtle, Screen
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

def move():
    for x in range(10):
        tim.speed('fast')
        tim.pencolor(color_list[random.randint(0, len(color_list) - 1)])
        tim.forward(1)
        tim.penup()
        tim.forward(130)
        tim.pendown()

def start(y):
    tim.penup()
    tim.goto(-600, y)
    tim.pendown()
    tim.forward(1)
    tim.penup()
    y += 100
    return y

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

tim = Turtle()
my_screen = Screen()
my_screen.colormode(255)

tim.pensize(50)
tim.speed('fastest')
tim.penup()
tim.goto(-600, -500)
tim.pendown()
tim.forward(1)
tim.penup()

y_position = -400

for x in range(10):
    move()
    if x < 9:
        y_position = start(y_position)


my_screen.exitonclick()