# 
# Prove 08: Word game
#
# Author: Estefania Ortiz
#

secret_word = "helaman"
guess = ""
count = 0

hint = ""

#initial hint
for a in secret_word:
    hint = hint + "_ "

print(f"Your hint is {hint}")

while guess != secret_word:

    same_lenght = False

    while(not same_lenght):
        guess = input("What is your guess? ").lower()
        count += 1

        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word. Please, make it better.")
        else:
            same_lenght = True

    if guess == secret_word:
        break
    
    hint = ""

    for i, a in enumerate(guess):
        letter = "_ "
        for j, b in enumerate(secret_word):
            
            if(a == b and i==j):
                letter = a.capitalize() + " "
            elif(a == b):
                letter = a + " "       

        hint = hint + letter
    
    print(f"Your hint is {hint}")

print(f"You guessed correctly in {count} guesses!")


        
