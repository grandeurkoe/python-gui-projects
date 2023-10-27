from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, paddle_coordinates):
        super().__init__()
        self.paddle_coordinates = paddle_coordinates
        self.generate_paddle()

    def generate_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.paddle_coordinates)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
