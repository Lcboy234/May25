import random
import turtle as t

tim = t.Turtle()

# change the colourmode
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)

# colors = ["lemonchiffon", "darkgoldenrod", "green", "cyan", "limegreen", "lightpink", "slategrey", "brown", "plum", "deeppink", "crimson"]
headings = [0, 90, 180, 270]

tim.pensize(10)

for i in range(100):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(headings))

screen = t.Screen()
screen.exitonclick()