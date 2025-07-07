import random
options=("Rock", "Paper", "Scissors")
computer = random.choice(options)

player = input ("Enter a choice (Rock, Paper, Scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")
