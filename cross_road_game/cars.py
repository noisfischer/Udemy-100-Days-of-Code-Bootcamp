from turtle import Turtle
import random


class Cars(Turtle):

    colors = ['yellow', 'pink', 'orange', 'blue', 'purple', 'green', 'red']

    def __init__(self):
        self.all_cars = []
        self.current_speed = 5

    def create_car(self):
        random_chance = random.randint(1, 2)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(0.5, 1.5)
            new_car.color(self.colors[random.randint(0, len(self.colors) - 1)])
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(320, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.current_speed)

    def speed_up(self, amount):
        self.current_speed = amount




