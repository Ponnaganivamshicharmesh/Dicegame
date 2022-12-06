import random

def greet():
    print("\n\n---------- GUESSING GAME ----------")
    print("This is a random guessing game, where you will be guessing a number between 1-6 ... ")

def printRules():
    print("\n\n---------- RULES ----------")
    print("1 => Roll the dice.")
    print("2 => Exit game.")

def goodbye():
    print("\n\nHave a Nice Day.\n")

score: int = 0
totalDiceThrows: int = 0

greet()
while True:
    printRules()
    choice: int = int(input("Your choice: "))
    if choice == 1:
        totalDiceThrows = totalDiceThrows+1
        print("Rolling dice ...")
        secret: int = random.randint(1, 6)
        guess: int = int(input("Guess the number (between 1 to 6): "))
        if guess == secret:
            score = score+1
            print("Yay, you guessed it!")
            print("Score: ", score)
        else:
            print("Wrong guess !!!")
    elif choice == 2:
        print("\n\nTotal score: ", score, "/", totalDiceThrows)
        goodbye()
        break
    else:
        print("\nWrong choice (choose 1 or 2).")