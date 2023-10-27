from turtle import Screen
from game_paddle import Paddle
from game_ball import Ball
from game_score_board import ScoreBoard
import time

game_window = Screen()
game_window.setup(width=800, height=600)
game_window.bgcolor("black")
game_window.tracer(0)
game_window.listen()


right_paddle = Paddle((365, 0))
left_paddle = Paddle((-365, 0))
ball = Ball()
score_board = ScoreBoard()

game_on = True

while game_on:
    game_window.update()
    time.sleep(ball.speed_counter)

    game_window.onkeypress(fun=right_paddle.move_paddle_up, key="Up")
    game_window.onkeypress(fun=right_paddle.move_paddle_down, key="Down")
    game_window.onkeypress(fun=left_paddle.move_paddle_up, key="w")
    game_window.onkeypress(fun=left_paddle.move_paddle_down, key="s")

    ball.move_ball()

    # Detect the collision between the ball and the wall.
    # Bounce the ball if it collides with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect the collision between the ball and the paddle.
    # Bounce the ball if it collides with the paddle.
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Detect when the ball is out of bounds.
    # If the right paddle misses.
    if ball.xcor() > 380:
        ball.home()
        ball.speed_counter = 0.1
        ball.bounce_x()
        score_board.l_increment()

    # If the left paddle misses.
    if ball.xcor() < -390:
        ball.home()
        ball.speed_counter = 0.1
        ball.bounce_x()
        score_board.r_increment()

game_window.exitonclick()
