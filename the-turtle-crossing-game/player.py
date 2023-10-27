from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.success_counter = 1
        self.speed_counter = 5
        self.generate_turtle()

    def generate_turtle(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        else:
            self.goto(STARTING_POSITION)
            self.success_counter += 1
            self.speed_counter += 10
