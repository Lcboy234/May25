import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

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

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    game_continue = True
    user_scores = -1
    computer_scores = -1

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_continue:
        user_scores = calculate_score(user_cards)
        computer_scores = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_scores}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_scores == 0 or computer_scores == 0 or user_scores > 21:
            game_continue = False
        else:
            more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
            if more_cards == "y":
                user_cards.append(deal_card())
            else:
                game_continue = False
    
    while computer_scores != 0 and computer_scores < 17:
        computer_cards.append(deal_card())
        computer_scores = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_scores}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_scores}")
    print(compare(user_scores, computer_scores))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()