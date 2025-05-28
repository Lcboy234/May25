import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    # starting the entire calculator with the logo
    print(art.logo)

    # state that accumulating equal true to start adding these calculation up
    accumulating = True

    # always ask for the first number
    first_number = float(input("What's the first number?: "))

    # while adding up calculation start printing out the operations key
    while accumulating:
        for key in operations:
            print(key)

        # ask user to pick an operation
        pick_operation = str(input("Pick an operation: "))

        # ask user to input the second number
        second_number = float(input("What's the next number?: "))

        # stating the result here so it can be printing out as in the next line together
        result = (operations[pick_operation](first_number, second_number))

        # print out the entire calculation out to show the user
        print(f"{first_number} {pick_operation} {second_number} = {result}")

        # ask the user whether they wanted to continue with the current result
        continue_or_not = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        
        # if they were to type y then the first number which is OUTSIDE OF THE WHILE LOOP will become the previous result
        if continue_or_not == "y":
            first_number = result

            # then we will ask them to pick the operation again which restarting the entire while loop
            accumulating = True
        
        elif continue_or_not == "n":
            # else do not accumate anymore if the user input is no
            accumulating = False

            # reprinting more space to cover the previous result
            print("\n" * 20)

            # restart the entire calculator to do new calculation
            calculator()
        
        else:
            print("you have the wrong input")
            
# this is to run the calculator
calculator()