import random
import json


with open("config.json", "r") as f:
    config = json.load(f)


def guessgame():
    to_guess = random.randint(
        config["min_guess"],
        config["max_guess"],
    )

    guesses = config["guesscount"]

    while True:
        print(f"You have {guesses} left, what is your guess?")

        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Well that was silly, way to waste a guess on a non-number!")
        else:
            if guess == to_guess:
                print("Yay you win!!!")
            else:
                print("Wrong!!1 ", end="")
                if guess < to_guess:
                    print("Guess higher ^_^")
                else:
                    print("Guess lower ._.")
        finally:
            guesses -= 1

        if guesses == 0:
            print("Out of guesses buddy!")
            break


def main():
    print("Welcome to THE GAME please make a pick:")
    print("(1) Guess a number!")
    choice = input("Enter number of game to play: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Could not understand your choice???")
        return

    if choice not in [1]:
        print("Could not understand your choice???")

    if choice == 1:
        guessgame()


if __name__ == "__main__":
    main()
