import random


def easy():
    randNum = random.randint(1, 10)
    for x in range(6):
        try:
            uInput = int(input("Make your guess: "))
        except:
            print("Please enter a number")
            break
        if uInput == randNum:
            print("You got it right")
            break
        else:
            print(f"That's wrong! You've got {5 - x} guesses left!")
    else:
        print("GAME OVER!")


def medium():
    randNum = random.randint(1, 20)
    for x in range(4):
        try:
            uInput = int(input("Make your guess: "))
        except:
            print("Please enter a number")
            break
        if uInput == randNum:
            print("You got it right")
            break
        else:
            print(f"That's wrong! You've got {3 - x} guesses left!")
    else:
        print("GAME OVER!")


def hard():
    randNum = random.randint(1, 50)
    for x in range(3):
        try:
            uInput = int(input("Make your guess: "))
        except:
            print("Please enter a number")
            break
        if uInput == randNum:
            print("You got it right")
            break
        else:
            print(f"That's wrong! You've got {2 - x} guesses left!")
    else:
        print("GAME OVER!")


uLevel = input("Kindly input level (easy, medium, hard): ")
if uLevel == "easy":
    easy()
elif uLevel == "medium":
    medium()
elif uLevel == "hard":
    hard()
else:
    "You failed to choose apropriate level, restart the game!"
