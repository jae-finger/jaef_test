import random

def main():
    print("hello and welcome to my game")
    numb = input("Please select a number between 1 and 100")
    if int(numb) <= 100:
        print("good job!")
    else:
        print("You fail!")

if __name__ == '__main__':
    main()
