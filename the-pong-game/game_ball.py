from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_x = 10
        self.move_y = 10
        self.speed_counter = 0.1
        self.generate_ball()

    def generate_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.speed_counter *= 0.9
