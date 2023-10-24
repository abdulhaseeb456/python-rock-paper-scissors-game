# Rock, Paper, Scissors Game in Python

import random

def play():
    print("\n------------------")
    choices = {
        "R": 'Rock',
        "P": 'Paper',
        "S": 'Scissors'
    }

    print(f"<> Valid Choices are:")
    for key, value in choices.items():
        print(f"\t- {key} for {value}")

    while True:
        try:
            user_choice = (input("\n<< Enter Your Choice: ")).upper()
        except ValueError:
            print('<? Invalid Choice')
 
        if user_choice in choices.keys():
            break
        else:
            print('<? Invalid Choice')

    random_choice = random.choice(list(choices.keys()))

    print(f"\n>< {choices[user_choice]} vs {choices[random_choice]}")

    if user_choice == random_choice:
        print(">> Game Ended in a draw!")
    else:
        matches = {
            ("R", "P"): 'R',
            ("R", "S"): 'R',
            ("P", "S"): 'S',
        }
        result = matches.get((user_choice, random_choice))
        if result is None:
            result = matches.get((random_choice, user_choice))

        if user_choice == result:
            print(">> Hey, you have won the game!")
        elif random_choice == result:
            print(">> Oh!, You Lost")

    print("------------------\n")


if __name__ == "__main__":
    play()
    while input("<> Press any key to exit and 'y' to play again: ").lower() == "y":
        play()
