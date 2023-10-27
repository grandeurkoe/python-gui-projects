from turtle import Turtle, Screen
from random import randint

red_turtle = Turtle(shape="turtle")
blue_turtle = Turtle(shape="turtle")
green_turtle = Turtle(shape="turtle")
yellow_turtle = Turtle(shape="turtle")
all_turtles = [red_turtle, blue_turtle, green_turtle, yellow_turtle]
colour = ["red", "blue", "green", "yellow"]
speed = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
is_race_on = False


def create_turtles():
    y_coordinates = -50
    for this_turtle in range(4):
        all_turtles[this_turtle].speed("fastest")
        all_turtles[this_turtle].penup()
        all_turtles[this_turtle].color(colour[this_turtle])
        all_turtles[this_turtle].goto(x=-240, y=y_coordinates)
        y_coordinates += 50


my_screen = Screen()
my_screen.setup(height=400, width=500)
my_bet = my_screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")
if my_bet:
    is_race_on = True

create_turtles()

while is_race_on:
    for each_turtle in all_turtles:
        if each_turtle.xcor() > 220:
            is_race_on = False
            winning_color = each_turtle.pencolor()
            if winning_color == my_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        each_turtle.forward(randint(1, 10))

my_screen.exitonclick()
