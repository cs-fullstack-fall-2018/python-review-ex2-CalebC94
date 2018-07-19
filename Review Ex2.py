import random


def main():
    randomNumber = random.randint(1,5)
    while True:
        guessedNumber = int(input("Guess the number"))
        if(guessedNumber == randomNumber):
            print("lucky guess")
            break
        else:
            print("Better luck next time")


main()