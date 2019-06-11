import random


def main():
    if input("Do you want to play a game? ") not in ["y", "Y"]:
        print("Couldn't understand you, please enter 'y' or 'Y'.")
        return

    to_guess = random.randint(10, 90)
    guesses = 5

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


if __name__ == "__main__":
    main()
