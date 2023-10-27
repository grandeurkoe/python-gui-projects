from colorgram import extract
from turtle import Turtle, Screen
from random import randint

my_dot = Turtle()
my_screen = Screen()
my_screen.colormode(255)
my_dot.hideturtle()
my_dot.speed(10)
my_dot.penup()
y_coordinates = - 180

colors = extract("hirst_painting_2.jpg", 10)
for row in range(10):
    my_dot.setpos(- 180, y_coordinates)
    y_coordinates += 50
    for column in range(10):
        my_dot.dot(20, colors[randint(0, 9)].rgb)
        my_dot.penup()
        my_dot.forward(50)

my_screen.exitonclick()
