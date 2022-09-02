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

#Write your code below this line 👇

import random

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

while player_choose > 2 or player_choose < 0:
    player_choose = int(input("Invalid options. Please type 0 for Rock, 1 for Paper or 2 for Scissors."))

options_list = [rock, paper, scissors]
player_icon = options_list[player_choose]

print(f"You choose {player_icon}")

computer_choose = random.randint(0, 2)
computer_icon = options_list[computer_choose]
print(f"Computer choose: {computer_icon}")

if player_choose == computer_choose:
    print("Draw")

else:
    #You are rock and computer is paper
    if player_choose == 0 and computer_choose == 1:
        print("You lose!")
    elif player_choose == 1 and computer_choose == 0:
        print("You win!")
    elif player_choose == 1 and computer_choose == 2:
        print("You lose!")
    elif player_choose == 2 and computer_choose == 1:
        print("You win!")
    elif player_choose == 0 and computer_choose == 2:
        print("You win!")
    elif player_choose == 2 and computer_choose == 0:
        print("You lose!")
    