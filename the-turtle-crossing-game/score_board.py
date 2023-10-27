from turtle import Turtle

FONT = ("Courier", 15, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.generate_scoreboard()

    def generate_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.goto(x=-270, y=260)
        self.write(arg=f"Level : {self.level}", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)
