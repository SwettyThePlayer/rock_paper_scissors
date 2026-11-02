import random

choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

player = input("rock, paper, scissors? ")
computer = random.choice(choices)

print(f"You: {player} | Computer: {computer}")

if player == computer:
    print("Draw!")
elif beats[player] == computer:
    print("You win!")
else:
    print("You lose!")

