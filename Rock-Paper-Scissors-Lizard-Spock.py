import random
option = ["rock", "paper", "scissors","lizard", "spock"]
print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")

rules = {  # Define rules of winning
    "rock": ["scissors", "lizard"],
    "paper": ["spock", "rock"],
    "scissors": ["paper", "lizard"],
    "spock": ["scissors", "rock"],
    "lizard": ["spock", "paper"]
}

def logic(choice1,choice2):
    #compare inputs
    if choice2 == choice1:
        return "Tie"
    elif choice2 in rules[choice1]:
        return "choice1_win"
    else:
        return "choice2_win"

while True:
    choice_user = input("Choose Rock, Paper, Scissors, Lizard, or Spock (type 'exit' to quit): \n")
    if choice_user == "exit":
        print("Thanks for playing! Bye!")
        break
    else:
        choice_com = random.choice(option)
        print(f"The computer chose {choice_com}")
        choice_user = choice_user.lower()
        result = logic(choice_user,choice_com)
        if result == "choice1_win":
            print(f"You won! {choice_user} beat {choice_com}.")
        elif result == "choice2_win":
            print(f"You lost! {choice_com} beat {choice_user}.")
        else:
            print("It's a tie!")
    process = input("Do you want to play again? (yes/no):\n")
    if process == "yes":
        continue
    elif process == "no":
        print("Thanks for playing! Bye!")
        break
