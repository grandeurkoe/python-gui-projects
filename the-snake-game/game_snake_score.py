from turtle import Turtle

SCORE_FONT = ("Optimus Princeps SemiBold", 14, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.score_board()

    def score_board(self):
        """Creates a score board for the snake game."""
        self.penup()
        self.sety(y=270)
        self.color("white")
        self.hideturtle()
        self.show_score()

    def show_score(self):
        """Prints the score board."""
        self.clear()
        self.read_high_score()
        self.write(arg=f"Score: {self.score} \t\t High Score: {self.high_score}", move=False, align="center", font=SCORE_FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.show_score()

    def score_after_meal(self):
        """Increments the score by 1 when the snake consumes food."""
        self.score += 1

    def read_high_score(self):
        with open("high_score.txt") as score_file:
            self.high_score = int(score_file.read())

    def write_high_score(self):
        with open("high_score.txt", mode="w") as score_file:
            score_file.write(str(self.high_score))
