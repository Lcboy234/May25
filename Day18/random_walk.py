import random
import turtle as t

tim = t.Turtle()

# change the colourmode
t.colormode(255)

tim.speed("fastest")

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return (red, green, blue)

def draw(gap):
        
    for i in range(int(360/ gap)):
        tim.color(random_color())
        tim.circle(100)

        tim.setheading(tim.heading() + gap)

draw(5)

screen = t.Screen()
screen.exitonclick()