
import guess.game as guess

while True:
    guess.runGame()

    play_again = input("Do you wanna play again?[y/n]: ")

    if play_again == "n":
        break

    elif play_again != "y" and play_again != "n":
        print("Sorry, that input is invalid.\n")

        play_again = input("Do you wanna play again?[y/n]: ")

        if play_again == "n":
            print("\n")
            break
