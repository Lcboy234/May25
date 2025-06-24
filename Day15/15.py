MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def check_resources_sufficient(choice_drink):
    for item in choice_drink:
        if choice_drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True

def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def check_transaction_successful(money_inputted, drink_cost):
    if money_inputted >= drink_cost:
        change = round(money_inputted - drink_cost, 2)
        print(f"Here is ${change} dollars in change. ")

        # to able to add in drink cost for money here therefore using global variable
        # because inside define outside variable cannot be used
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name}.Enjoy!")


machine_running = True

while machine_running:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        machine_running = False
    
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")

    else:
        drink = MENU[choice]
        if check_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])