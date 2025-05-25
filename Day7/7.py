import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)

# to determine to while loop
game_over = False

# keep the empty list outside of while loop so it will continue getting updated but not wiped out
correct_letters = []

while not game_over:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("guess a letter. ").lower()

    if guess in correct_letters:
        print("You have already guessed this.")

    display = ""

    # for every letter in chosen word
    for letter in chosen_word:
        # if guessed word matched with letter from chosen word
        if guess == letter:
            # display must add it to its string
            display += guess

            # correct_letters must add it to its list
            correct_letters.append(guess)

        # if letter are already in correct_letters
        elif letter in correct_letters:
            # display should add it back into its string
            display += letter
        # else print as empty inside display
        else:
            display += "_"

    # print the entire display
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"{chosen_word} is the correct word.")
            print(f"***********************YOU LOSE**********************")

    # until no more _ inside display the while loop is over
    if "_" not in display:
        game_over = True
        print("you win")

    print(stages[lives])