# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# screen = Screen()
# screen.exitonclick()


# for i in range(8):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

from turtle import *

tim = Turtle()

def draw(num_sides):

    angle = 360/ num_sides
    
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape in range(3, 11):
    draw(shape)

screen = Screen()
screen.exitonclick()