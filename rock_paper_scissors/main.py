import random 

print("Welcome to the rock, paper, scissors game :)")


player_choice = input("Choose one: rock, paper, scissors: ").strip().lower()


choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

# I collected the winning possibilities in a dictionary.
winning_combinations = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}


if player_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
elif player_choice == computer_choice:
    print(f"It's a draw! Both chose {computer_choice}.")
elif winning_combinations[player_choice] == computer_choice:
    print(f"You win! Your {player_choice} beats {computer_choice}.")
else:
    print(f"You lose! Computer's {computer_choice} beats your {player_choice}.")


"""
Created By: Aytuğ Yürük.

"""