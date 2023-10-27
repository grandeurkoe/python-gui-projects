from turtle import Screen
from game_snake import Snake
from game_snake_food import Food
from random import randrange
from game_snake_score import Score
from game_playable_area import PlayArea
import time

game_window = Screen()
game_window.setup(width=600, height=600)
game_window.bgcolor("gray0")
game_window.title("The Snake Game")
# Turn off the animation by passing an argument of '0' to the tracer() function.
game_window.tracer(0)

play_area = PlayArea()
snake = Snake()
food = Food()
score = Score()

game_window.listen()
game_window.onkeypress(snake.up, "Up")
game_window.onkeypress(snake.down, "Down")
game_window.onkeypress(snake.left, "Left")
game_window.onkeypress(snake.right, "Right")

game_in_session = True
while game_in_session:
    # Updates the window after all the snake parts have moved 20 pixels forward.
    game_window.update()
    # From the time module, we use the sleep() function to delay the game_window by 0.1 second.
    # Removing the sleep function causes the snake to move too fast.
    time.sleep(0.1)

    snake.move()

    # Detect collision of the snake with food.
    if snake.snake[0].distance(food) < 15:
        food.setposition(x=randrange(-260, 260, 10), y=randrange(-260, 260, 10))
        snake.grow_snake()
        score.score_after_meal()
        score.show_score()

    # Detects collision of the snake with wall.
    if snake.snake[0].xcor() > 270 or snake.snake[0].xcor() < -270 or snake.snake[0].ycor() > 270 or snake.snake[0].ycor() < -270:
        score.reset_score()
        snake.reset_snake()

    # Detect collision of the snake with tail.
    for snake_segment in snake.snake[1:len(snake.snake)]:
        if snake.snake[0].distance(snake_segment) < 10:
            score.reset_score()

game_window.exitonclick()
