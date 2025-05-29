import random
import art

# to choose the cards from a list using random.choice
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# to calculate the score of cards in the list using sum()
def calculate_score(cards):

    # if total of list is equal to 21 then return 0
    if sum(cards) == 21:
        # return terminates the if here
        return 0
    
    # starting a new if function for situation when 11 is in the list and total in list is adding up more than 21
    if 11 in cards and sum(cards) > 21:
        # remove 11 from list
        cards.remove(11)
        # add 1 to list
        cards.append(1)

    # else if none of the top "if" situation appear add up the total from list 
    return sum(cards)

# this function is to print out the statement of if the result is win or lose or draw
def compare(left_score, right_score):
    if left_score == right_score:
        return "draw"
    elif right_score == 0:
        return "you lose"
    elif left_score == 0:
        return "you win"
    elif left_score > 21:
        return "you lose"
    elif right_score > 21:
        return "you win"
    elif left_score > right_score:
        return "you win"
    else:
        return "you lose"

# use a function to start the game
def play_game():

    # by following the final game plan it should start printing out the logo first
    print(art.logo)

    # set both user and computer cards to empty list so we can append numbers to this empty list
    user_cards = []
    computer_cards = []

    # boolean function for while loop
    game_continue = True

    # this is to set the user and computer score to -1 therefore it doesn't start with 0 and ended the game with blackjack
    user_scores = -1
    computer_scores = -1

    # set the range to 2 so everytime we are adding two numbers to both user and computer lists
    # dont add this into the while loop so the numbers in list doesn't change
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # when the game starting in while loop
    while game_continue:

        # we always calculate the scores of both user and computer
        user_scores = calculate_score(user_cards)
        computer_scores = calculate_score(user_cards)

        # printing out the current user cards and scores with the first computer card only therefore user can think if they wanted to add more cards
        print(f"Your cards: {user_cards}, current score: {user_scores}")
        print(f"Computer's first card: {computer_cards[0]}")

        # when user or computer blackjack or user score is more than 21 then the game ends
        if user_scores == 0 or computer_scores == 0 or user_scores > 21:
            game_continue = False
        else:
            # else ask the user if they needs more cards by typing 'y' in for input
            more_cards = input("Type 'y' to get another card, type 'n' to pass: ")

            # if input is equal to 'y'
            if more_cards == "y":

                # draw one more card for the user
                # when the user_score not reaching more than 21 the game will still continue and ask user if they needs more cards
                user_cards.append(deal_card())
            else:

                # other wise when input is 'n' then game should end
                game_continue = False
    
    # top while loop is mainly for user however
    # this bottom while loop is for computer
    # computer will keep drawing cards when their score is not equal to 0 and less than 17
    while computer_scores != 0 and computer_scores < 17:
        computer_cards.append(deal_card())

        # calculate final computer score here when the cards are fully drawn
        computer_scores = calculate_score(computer_cards)
    
    # print out user final hands and scores to show
    print(f"Your final hand: {user_cards}, final score: {user_scores}")

    # print out final hand for computer following the second while loop
    print(f"Computer's final hand: {computer_cards}, final score: {computer_scores}")

    # compare the scores and show if the user win or lose or draw
    print(compare(user_scores, computer_scores))

# final while loop is to ask user if they want to play a game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)

    # once they type in 'y'
    # run the play game function and start printing logo again and calculate both cards and scores
    play_game()
    