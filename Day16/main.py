# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward

# my_screen = Screen()

# # this is object attributes(variable)
# print(my_screen.canvheight)
# # this is methods(function)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

# this is methods
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# this is attributes
table.align = "l"
print(table)