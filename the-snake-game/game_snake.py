from turtle import Turtle

MOVE_SNAKE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.generate_snake()

    def generate_snake(self):
        horizontal_coordinate = 0
        # Creates the three parts of the snake and places them in an appropriate position on the game_window.
        for snake_part in range(3):
            self.snake.append(Turtle(shape="square"))
            self.snake[snake_part].penup()
            self.snake[snake_part].color("white")
            self.snake[snake_part].setx(horizontal_coordinate)
            horizontal_coordinate -= 20

    def grow_snake(self):
        self.snake.append(Turtle(shape="square"))
        snake_tail = len(self.snake) - 1
        self.snake[snake_tail].penup()
        self.snake[snake_tail].color("white")
        self.snake[snake_tail].setposition(x=self.snake[snake_tail - 1].xcor(), y=self.snake[snake_tail - 1].ycor())

    def reset_snake(self):
        for each_snake_part in self.snake:
            each_snake_part.goto(1000, 1000)
        self.snake.clear()
        self.generate_snake()

    def move(self):
        # Moves the previous snake part to the next snake part from the back end.
        for move_part in range(len(self.snake) - 1, 0, -1):
            self.snake[move_part].setposition(x=self.snake[move_part - 1].xcor(), y=self.snake[move_part - 1].ycor())

        self.snake[0].forward(MOVE_SNAKE)

    def up(self):
        if self.snake[0].heading() == 270.0:
            self.snake[0].setheading(270)
        else:
            self.snake[0].setheading(90)
            self.move()

    def down(self):
        if self.snake[0].heading() == 90.0:
            self.snake[0].setheading(90)
        else:
            self.snake[0].setheading(270)
            self.move()

    def left(self):
        if self.snake[0].heading() == 0.0:
            self.snake[0].setheading(0)
        else:
            self.snake[0].setheading(180)
            self.move()

    def right(self):
        if self.snake[0].heading() == 180.0:
            self.snake[0].setheading(180)
        else:
            self.snake[0].setheading(0)
            self.move()
