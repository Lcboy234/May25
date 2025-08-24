# import colorgram

# list = []

# colors = colorgram.extract("./Day18/image.jpg", 30)

# for every_single_color in colors:
#     r = every_single_color.rgb.r
#     g = every_single_color.rgb.g
#     b = every_single_color.rgb.b
#     new_color = (r, g, b)

#     list.append(new_color)

# print(list)

import turtle as t
import random

t.colormode(255)

final_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()

tim.speed("fast")

# take the pen up before drawing
tim.penup()

# hide the turtle which is also the arrow
tim.hideturtle()

# make sure tim is going to the left bottom corner

# set its heading to the left bottom

# from 0 starting at east to 270 south as anticlockwise

tim.setheading(225)

# move it by 250 range
tim.forward(325)

# rehead it back to east
tim.setheading(0)

# 10 x 10 = 100
number_of_dots = 100

# get it to run in range of 10 because of the 10 multiply by 10 setting
for dot_count in range(1, number_of_dots + 1):

    tim.dot(20, random.choice(final_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        # face top
        tim.setheading(90)
        # move by 50
        tim.forward(50)
        # face left
        tim.setheading(180)
        # move back to the left
        tim.forward(500)
        # turn back facing east
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()