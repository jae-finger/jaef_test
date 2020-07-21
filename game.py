import random

numb = random.randint(1, 100)
guess = -1

def main():
    print("hello and welcome to my game")
    guess = input("Please select a number between 1 and 100")
    # if int(numb) <= 100:
    #     print("good job!")
    # else:
    #     print("You fail!")
    print(f"You guessed {guess}\n")
    print(f"The computer's actual choice was: {numb}")

if __name__ == '__main__':
    main()
