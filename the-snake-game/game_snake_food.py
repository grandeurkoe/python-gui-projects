from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        # Creates a circle of 20 * 20 size.
        self.shape("circle")
        self.penup()
        # Reduces the size of circle to 10 * 10 size.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        # Sets the circle to a random (x,y) position in the 600 * 600 coordinate plane.
        self.setposition(x=randrange(-260, 260, 10), y=randrange(-260, 260, 10))
