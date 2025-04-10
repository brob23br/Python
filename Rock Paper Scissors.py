from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
computer_move = num

# Ask a user to enter their move
user_move = input("Select rock, paper, or scissors: ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if user_move == "rock":
    print(f"You selected {rock}")
elif user_move  == "paper":
    print(f"You selected {paper}")
elif user_move == "scissors":
    print(f"You selected {scissors}")
else:
    print("invalid selection")

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
if computer_move == 1:
    print(f"Computer selected {rock}")
elif computer_move == 2:
    print(f"Computer selected {paper}")
elif computer_move == 3:
    print(f"Computer selected {scissors}")
else:
    print("invalid selection")

# Figure out who wins and print the result!
if (user_move == "rock" and computer_move == 2) or (user_move == "paper" and computer_move == 3) or (user_move == "scissors" and computer_move == 1):
    print("Computer Wins!")
elif (user_move == "rock" and computer_move == 1) or (user_move == "paper" and computer_move == 2) or (user_move == "scissors" and computer_move == 3):
    print("It's a Tie!")
else:
    print("You Win!")
