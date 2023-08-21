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

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print("Choice out of range.")

computer = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print("Computer chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

if (player == 0) and (computer_choice == 2):
  print("You win!")
elif (player == 2) and (computer_choice == 1):
  print("You win!")
elif (player == 1) and (computer_choice == 0):
  print("You win!")
elif (player == computer_choice):
  print("It's a tie!")
else:
  print("You lose!") 