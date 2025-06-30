import random

guess = ""

play = "yes"

while play == "yes":
    magic_number = random.randint(1, 100)


    while guess != magic_number:
        guess = int(input("What is your guess? "))

        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")

    play = input("Would you like to play again (yes/no)?")

print("Thank you for playing. Goodbye.") 