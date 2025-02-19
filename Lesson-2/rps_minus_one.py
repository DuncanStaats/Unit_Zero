import random 
"""
Name: Duncan Staats
File: rps_minus_one.py
Description: Implements the Rock Paper Scissor Minus Onegame from Squid Game
"""

"""
pseudocode
set comp score and player score to 0
Have computer pick to random "hands" of rps
Store values in comp_hand somehow (you choose)
Ask user for their hands
store calues in player_hand
Ask user which hand to keep
computer randomly chooses hand
evaluate who wins
update score
ask if they want to continue or quit
if quit, print scores and end game
else play agian
"""

def main():
    
    comp_score = 0
    player_score = 0

    while True:

        comp_hand1 = random.randint(1,3)
        comp_hand2 = random.randint(1,3)

        if comp_hand1 == 1:
            comp_hand1 = "Paper"
        elif comp_hand1 == 2:
            comp_hand1 = "Rock"
        elif comp_hand1 == 3:
            comp_hand1 = "Scissors"

        if comp_hand2 == 1:
            comp_hand2 = "Paper"
        elif comp_hand2 == 2:
            comp_hand2 = "Rock"
        elif comp_hand2 == 3:
            comp_hand2 = "Scissors"

        player_hand1 = input("What is your first hand(Rock, Paper, or Scissor): ")
        player_hand2 = input("What is your second hand(Rock, Paper, or Scissor): ")
        
        player_hand1 = player_hand1.title()
        player_hand2 = player_hand2.title()

        print()
        print(f"The computers hands are {comp_hand1} and {comp_hand2}. Your hands are {player_hand1} and {player_hand2}."
            f"\nNow that you know which hands the computer could play, which one of your hands will you KEEP.")

        player_result = int(input(f"Which hand number will you keep(Enter in the corresponding number), 1 = {player_hand1} and 2 = {player_hand2}: "))
        
        if player_result == 1:
            player_result = player_hand1
        elif player_result == 2:
            player_result = player_hand2


        comp_result = random.randint(1,2)
        if comp_result == 1:
            comp_result = comp_hand1
        elif comp_result == 2:
            comp_result = comp_hand2

        print()
        print(f"Your hand is {player_result} and the compter's hand is {comp_result}.")

        if player_result == "Rock":
            if comp_result == "Rock":
                print("Tie")
            elif comp_result == "Paper":
                print("Lose")
                comp_score += 1
            elif comp_result == "Scissors":
                print("Win")
                player_score += 1
        elif player_result == "Paper":
            if comp_result == "Rock":
                print("Win")
                player_score += 1
            elif comp_result == "Paper":
                print("Tie")
            elif comp_result == "Scissors":
                print("Lose")
                comp_score += 1
        elif player_result == "Scissors":
            if comp_result == "Rock":
                print("Lose")
                comp_score += 1
            elif comp_result == "Paper":
                print("Win")
                player_score += 1
            elif comp_result == "Scissors":
                print("Tie")

        print(f"Your score is {player_score}")
        print(f"Computer score is {comp_score}")

        again = int(input("Will you play again(1 for yes, 2 for no): "))

        if again == 1:
            continue
        elif again == 2:
            break

main()