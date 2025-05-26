# TODO-1: Import and print the logo from art.py when the program starts.

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, encode_or_decode):
    # set an empty string for ciphertext
    final_text = ""

    # check every letter for inputted string
    for letter in original_text:
        if letter not in alphabet:
            final_text += letter

        if encode_or_decode == "encode":
            # for example: alphabet = ['a', 'b', 'c', 'd', 'e']
            # using alphabet.index(letter) can check current position of letter
            # for example: alphabet.index("a") = 0
            # by adding shift amount to it by 2 
            # it will become c

            # set a variable for the current shifted position
            shifted_forward_position = alphabet.index(letter) + shift_amount

            # for example: in order to shift z back to a after shift amount of 9
            # which is 25(current position of z) and add 9 to it
            # it then add up to 34 which isn't in the range of this list
            # therefore using remainder 34 % 25 = 9
            # which will return z back to the front

            shifted_forward_position = shifted_forward_position % len(alphabet)

            # add back shifted position string back to ciphertext using +=
            # alphabet[] to find the actual string but not index() to find the position(int) of it
            final_text += alphabet[shifted_forward_position]

        if encode_or_decode == "decode":
            shifted_backward_position = alphabet.index(letter) - shift_amount
            shifted_backward_position %= len(alphabet)
            final_text += alphabet[shifted_backward_position]

    print(final_text)

# TODO-3: Can you figure out a way to restart the cipher program?

game_over = False

while not game_over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == "no":
        game_over = True
        print("Goodbye")