import random

choices = ["rock", "paper", "scissors", "lizard", "spock"]
beats = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}
player_score = 0
computer_score = 0

while player_score < 3 and computer_score < 3:
    player = input("rock, paper, scissors? ").lower().strip()
    while player not in choices:
        player = input("Please type rock, paper or scissors. ")
    computer = random.choice(choices)

    print(f"You: {player} | Computer: {computer}")

    if player == computer:
        print("Draw!")
    elif computer in beats[player] == computer:
        print("You win the round!")
        player_score +=1
    else:
        print("You lose the round!")
        computer_score +=1

    print(f"Score: You {player_score} - {computer_score} Computer")
    print()

if player_score == 3:
    print("YOU WIN THE GAME!")
else:
    print("The computer has defeated you. Try again!")