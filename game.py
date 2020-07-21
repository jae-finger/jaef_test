import random

# numb = random.randint(1, 100)
numb = 50
guess = -1


def main():
    print("Hello and welcome to my test game!")
    guess = input("Please select a number between 1 and 100\n")
    guess = int(guess)
    if 100 >= guess >= 1:
        if guess > numb:
            print(f"Your guess is too high, the computer guessed {numb}")
        elif guess < numb:
            print(f"Your guess is too low, the computer guessed {numb}")
        elif guess == numb:
            print(f"You guessed {guess} and the computer had the number {numb} selected. Great job!")
        else:
            print("You selected a number but something went wrong :(")
    else:
        print("You didn't select a number :(")


if __name__ == '__main__':
    main()
