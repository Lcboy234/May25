# # from turtle import Turtle, Screen

# # timmy = Turtle()
# # print(timmy)
# # timmy.shape("turtle")
# # timmy.color("red")
# # timmy.forward

# # my_screen = Screen()

# # # this is object attributes(variable)
# # print(my_screen.canvheight)
# # # this is methods(function)
# # my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()

# # this is methods
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# # this is attributes
# table.align = "l"
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)