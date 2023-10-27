import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import ScoreBoard
MOVE_DISTANCE = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
current_loop = 0

player_turtle = Player()
all_cars = [CarManager()]
score = ScoreBoard()

playing_the_game = True
while playing_the_game:
    current_loop += 1
    time.sleep(0.1)
    screen.update()
    screen.onkey(fun=player_turtle.move_turtle, key="Up")
    score.level = player_turtle.success_counter
    movement_speed = player_turtle.speed_counter
    score.clear()
    score.generate_scoreboard()
    for cars in all_cars:
        cars.move_cars(movement_speed)
        if cars.distance(player_turtle) < 20:
            playing_the_game = False
            score.game_over()
    if current_loop % 6 == 0:
        all_cars.append(CarManager())


screen.exitonclick()
