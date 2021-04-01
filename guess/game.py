
import random


def chooseDifficulty():
    easy = random.randint(0, 10)
    medium = random.randint(0, 25)
    hard = random.randint(0, 50)

    print("\n-----GUESS A NUMBER!-----")

    print("\n\nChoose a difficulty: ")
    print("[1] Easy: 0 - 10")
    print("[2] Medium: 0 - 25")
    print("[3] Hard: 0 - 50")

    while True:
        difficulty = input(">> ")

        if difficulty == "1":
            number = easy
            return number

        elif difficulty == "2":
            number = medium
            return number

        elif difficulty == "3":
            number = hard
            return number

        elif difficulty != 1 or difficulty != 2 or difficulty != 3:
            print("Sorry, that input is invalid.\n")
            continue

        break


def runGame():
    number = chooseDifficulty()

    while True:
        try:
            guess = input("Guess a number: ")

            if int(guess) > number:
                print("Too High! Try a lower number.\n")

            elif int(guess) < number:
                print("Too Low! Try a higher number.\n")

            elif int(guess) == number:
                print("Congratulations! You guessed the right number!\n")
                break

        except ValueError:
            print("Sorry, that input is invalid.\n")
