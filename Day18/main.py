# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# screen = Screen()
# screen.exitonclick()

from turtle import *

tim = Turtle()

for i in range(8):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()