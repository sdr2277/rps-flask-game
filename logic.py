# logic.py
import random

def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    if user_choice == computer:
        result = "draw"
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer == "paper"):
        result = "win"
    else:
        result = "lose"

    return {"user": user_choice, "computer": computer, "result": result}
