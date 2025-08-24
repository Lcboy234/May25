import random
from turtle import *

tim = Turtle()

colors = ["lemonchiffon", "darkgoldenrod", "green", "cyan", "limegreen", "lightpink", "slategrey", "brown", "plum", "deeppink", "crimson"]
headings = [0, 90, 180, 270]

tim.pensize(10)

for i in range(100):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(headings))

screen = Screen()
screen.exitonclick()