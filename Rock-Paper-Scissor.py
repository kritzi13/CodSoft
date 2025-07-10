import random

print("Let's play 🪨 / 📄 / ✂️!")


options = ("rock", "paper", "scissor")

comp_win =["Ouch! The computer outsmarted you this time!", "Better luck next round, human!", "The machine wins... for now.", "You just got paper-cut by the computer!", "Rocked, socked, and shocked — the computer wins!", "The robot reigns supreme!", "Defeated by circuits and code!", "You're gonna let a bunch of 1s and 0s beat you?"]

user_win= ["Boom! Human intelligence wins!","Take that, tin can!", "Computer.exe has stopped working — you win!", "Score one for the meatbags!", "Rust in peace, robot. You lost!", "Even algorithms can't beat human instincts!", "System failure... user victory detected!", "You outplayed the machine. Nice!"]

draw =["Great minds think alike!", "It's a tie! Try again, warrior!", "Deadlock! No winner this time.", "Same move, same brainwave!","Nobody wins, nobody loses — yet."]

play = True

while play:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Pick: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print(random.choice(draw))
    elif player == "rock" and computer == "scissors" :
        print(random.choice(user_win))
    elif player == "paper" and computer == "rock":
        print(ranodm.choice(user_win))
    elif player == "scissors" and computer == "paper":
        print(ranodm.choice(user_win))
    else:
        print(random.choice(comp_win))

    game = input("Playe again? (y/n): ").lower()
    if not game == "y":
        play = False

print("Thanks for playing..")
