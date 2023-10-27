from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_cars()

    def generate_cars(self):
        for all_cars in range(5):
            self.shape("square")
            self.shapesize(stretch_len=2, stretch_wid=1)
            self.color(choice(COLORS))
            self.penup()
            self.goto(x=310, y=randint(-250, 250))
            self.setheading(180)

    def move_cars(self, move_distance):
        self.forward(move_distance)
