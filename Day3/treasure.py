print("Welcome to the Trasure island.")

first_choice = input("left or right? ").lower()

if first_choice == "left":
    second_choice = input("swim or wait? ").lower()
    if second_choice == "wait":
        third_choice = input("which door? red, yellow, or blue? ").lower()
        if third_choice == "yellow":
            print("you win")
        else:
            print("game over")
    elif second_choice == "swim":
        print("game over")
    else:
        print("wrong input")
elif first_choice == "right":
    print("game over")
else:
    print("wrong input")


