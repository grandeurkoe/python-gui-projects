from turtle import Turtle


class PlayArea(Turtle):
    def __init__(self):
        super().__init__()
        self.generate_play_area()

    def generate_play_area(self):
        self.resizemode(rmode="user")
        self.shape("square")
        self.color("grey10")
        self.turtlesize(stretch_wid=27, stretch_len=27, outline=1)

