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


def reboot():
    code = input("Please enter your reboot token: ")

    if code != config["reboot_token"]:
        print("Wrong reboot token!")
        return

    print("Rebooting")
    subprocess.run(["shutdown", "-r", "now"])
    raise SystemExit(0)


def main():
    while True:
        print("Welcome to THE GAME please make a pick:")
        print("(0) Exit!")  
        print("(1) Guess a number!")
        print("(2) Reboot the game server!")

        choice = input("Enter number of game to play: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Could not understand your choice???")
            return

        if choice not in [0, 1, 2]:
            print("Could not understand your choice???")

        if choice == 0:
            return
        elif choice == 1:
            guessgame()
        elif choice == 2:
            reboot()


if __name__ == "__main__":
    main()
