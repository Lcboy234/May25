from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def anti_clockwise():
    tim.setheading(tim.heading() + 10)

def clockwise():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    # going back without dragging pen mark
    tim.penup()
    tim.home()
    # put the pen back down for next drawing
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(anti_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()