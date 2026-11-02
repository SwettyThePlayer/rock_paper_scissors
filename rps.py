import random

choices = ["rock", "paper", "scissors"]

player = input("rock, paper, scissors?")
computer = random.choice(choices)

print(f"You chose: {player}")
print(f"The computer chose: {computer}!")
