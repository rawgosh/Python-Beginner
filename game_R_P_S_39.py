#Rock paper scissor

import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices) #selecting a random choice
    player = input("rock, paper, scissors? :").lower()
    if player == computer:
        print("Player :"+player.capitalize())
        print("Computer :"+computer.capitalize())
        print("It's a draw.\n")
    elif player == "rock" and computer == "paper" or player == "paper" and computer == "scissors" or player == "scissors" and computer == "rock":
        print("Player :"+player.capitalize())
        print("Computer :"+computer.capitalize())
        print("Computer wins.\n")
    elif player == "paper" and computer == "rock" or player == "scissors" and computer == "paper" or player == "rock" and computer == "scissors":
        print("Player :"+player.capitalize())
        print("Computer :"+computer.capitalize())
        print("You win.\n")
    else:
        print("That is not in the choice.\n")
    
    play_again = input("Wanna play again? Y/YES or N/NO :").lower()

    if play_again == "yes" or play_again =="y":
        continue
    elif play_again == "no" or play_again == "n":
        break
    else:
        print("\nThe game is terminated by default for choosing error choice to play again please start the game.\n")
        break
print("Lets play sometime soon :)")

