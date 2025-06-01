import art
import random

# setting global scope in full cap that cannot be changed in value
EASY_LEVEL = 10
HARD_LEVEL = 5

# let the user choose the level by either easy or hard
def choose_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        # if choice is easy then return 10 which is the easy level
        return EASY_LEVEL
    
    elif choice == "hard":
        # if not then return hard which is 5 in value
        return HARD_LEVEL

# define function to compare user guess and actual answer with turns that is going to be related with GLOBAL SCOPE
def compare(user_guess, actual_answer, turns):
    if user_guess < actual_answer:
        # if user guess is less than actual answer print too low
        print("Too low.")
        # and then return the turns to be minus 1
        return turns - 1
    
    elif user_guess > actual_answer:
        # same if the user guess is higher than actual answer
        print("Too high.")
        return turns - 1

    else:
        # otherwise print that the user got the correct guess which is equal to the actual answer
        print(f"You got it! The answer was {actual_answer}.")

# define game to start the game
def game():
    # print out the logo first
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # set a answer variable that randomise from 1 to 100
    answer = random.randint(1, 101)

    # the starting turns will be equal to choose difficulty function which is going to either return 5 or 10
    starting_turns = choose_difficulty()

    # starting guess is equal to 0
    guess = 0

    # when the answer is randomised, starting guess is equal to 10, which means guess is not equal to answer
    while guess != answer:
        # it then print out the starting level which is 5 or 10
        print(f"You have {starting_turns} attempts remaining to guess the number.")

        # user can user guess variable as an input
        guess = int(input("Make a guess: "))

        # this starting turns is the LOCAL SCOPE that will change the starting_turns on top from 10 to 9 to 8 to 7 based on compare function
        starting_turns = compare(guess, answer, starting_turns)

        # when starting turns on top "starting_turns = choose_difficulty()" reached 0 print game over and use return to end the game
        if starting_turns == 0:
            print("Game over")
            return
        
        # else when guess is not equal to answer, loop back to the top, 
        # print remaining turns and tell user to make another guess then 
        # compare the value to see if starting turns decrease to 0 itself
        elif guess != answer:
            print("Try again")

game()