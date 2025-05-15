import random
    
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]


human_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

print(hand[human_choice])


print("Computer chose:")


computer_choice = random.randint(0, 2)

print(hand[computer_choice])


if human_choice == 0 and computer_choice == 2:
    print("you win")

elif human_choice == 2 and computer_choice == 0:
    print("you lose")

elif human_choice > computer_choice:
    print("you win")

elif human_choice == computer_choice:
    print("draw")

elif computer_choice > human_choice:
    print("you lose")

else:
    print("wrong input")