import art
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def choose_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == "easy":
        return EASY_LEVEL
    
    elif choice == "hard":
        return HARD_LEVEL

def compare(user_guess, actual_answer, turns):
    if user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    
    elif user_guess > actual_answer:
        print("Too high.")
        return turns - 1

    else:
        print(f"You got it! The answer was {actual_answer}.")

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 101)
    starting_turns = choose_difficulty()

    guess = 0

    while guess != answer:
        guess = int(input("Make a guess: "))
        remaining_turns = compare(guess, answer, starting_turns)
        if remaining_turns == 0:
            print("Game over")
            # end 
            return
        elif guess != answer:
            print("Try again")

game()