import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

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
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print("****************************<???>/6 LIVES LEFT****************************")
    guess = input("guess a letter. ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

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

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")

    # until no more _ inside display the while loop is over
    if "_" not in display:
        game_over = True
        print("you win")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py

    print(stages[lives])