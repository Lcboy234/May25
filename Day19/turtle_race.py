from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_choice = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_choice)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for different_turtles in range(0, 6):
    new_turtle = Turtle(shape = "turtle")

    # .color for colors[0], colors[1], colors[2] and more
    new_turtle.color(colors[different_turtles])

    new_turtle.penup()

    # y position is showing y[0], y[1], y[2] and more
    new_turtle.goto(x = -230, y = y_positions[different_turtles])

    # appending each of the new turtle
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for moving_turtle in all_turtles:
        if moving_turtle.xcor() > 230:
            is_race_on = False
            winning_color = moving_turtle.pencolor()

            if winning_color == user_choice:
                print(f"You've won! The {winning_color} is the winning turtle")
            else:
                print(f"You've lost! The {winning_color} is the winning turtle")
                
        random_distance = random.randint(0, 10)
        moving_turtle.forward(random_distance)

screen.exitonclick()