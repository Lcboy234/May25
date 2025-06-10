from art import logo, vs
from game_data import data
import random


# formatting out the data from anothe python file
def format_data(account):

    # formatting the data from other python file using dictionary format
    # account_name = account["name"] will take in all the name by passing the data argument into account
    account_name = account["name"]

    # same for description
    account_description = account["description"]

    # and country
    account_country = account["country"]

    # at the end of definition use return to print out its entire format
    # this is to always print out the sentences for vs
    return f"{account_name}, a {account_description}, from {account_country}."


# comparing first account and second account
def compare(user_guess, a_followers, b_followers):
    if a_followers > b_followers:

        # return a as correct
        return user_guess == "a"
    else:

        # return b as correct
        return user_guess == "b"


print(logo)
game_is_on = True

# set this for account a
second_account = random.choice(data)
score = 0

# while game is on is True

"""
the game wont touch the thing at the top which is outside of while loop
""" 

while game_is_on:

    # equal to the top one
    first_account = second_account

    # the actual account b
    second_account = random.choice(data)


    # this is an if condition when they are the same 
    if first_account == second_account:
        second_account = random.choice(data)
    
    print(f"Compare A: {format_data(first_account)}")

    print(vs)

    print(f"Compare B: {format_data(second_account)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    """
    clear the screen after input
    """

    print("\n" * 20)
    print(logo)

    first_account_follower = first_account["follower_count"]
    second_account_follower = second_account["follower_count"]

    correct = compare(guess, first_account_follower, second_account_follower)


    if correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        # if not correct end the game
        game_is_on = False