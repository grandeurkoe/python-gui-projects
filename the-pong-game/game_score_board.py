from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.generate_score_board()

    def generate_score_board(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_increment(self):
        self.l_score += 1
        self.generate_score_board()

    def r_increment(self):
        self.r_score += 1
        self.generate_score_board()
