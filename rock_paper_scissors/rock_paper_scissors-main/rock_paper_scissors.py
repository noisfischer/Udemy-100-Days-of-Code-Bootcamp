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

#Write your code below this line 👇

player_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computer_choice = random.randint(0, 2)

game_list = [rock, paper, scissors]

print(f"You chose\n{game_list[player_choice]}")
print(f"The computer chose\n{game_list[computer_choice]}")

if player_choice == computer_choice:
  print("IT'S A TIE!")
elif player_choice == 0 and computer_choice == 1:
  print("YOU LOSE!")
elif player_choice == 0 and computer_choice == 2:
  print("YOU WIN!")
elif player_choice == 1 and computer_choice == 0:
  print("YOU WIN!")
elif player_choice == 1 and computer_choice == 2:
  print("YOU LOSE!")
elif player_choice == 2 and computer_choice == 0:
  print("YOU LOSE!")
else:
  print("YOU WIN!")