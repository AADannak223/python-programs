import random

no_for_guess = random.randint(1, 100)

no_of_guesses = 1
print("*** You have only 9 chance to guess the number ***")

if no_for_guess < 50:
    while no_of_guesses <= 9:
        guess_no = int(input("\nGuess the number : "))
        if guess_no > no_for_guess:
            print("Please enter small number")

        elif no_for_guess > guess_no:
            print("Please enter greater no ")

        else:
            print("congratulation you won!!!")
            print(no_of_guesses, " no of guesses you took to finish")
            break

        print(9 - no_of_guesses, "Number of guesses left")
        no_of_guesses = no_of_guesses + 1
        if no_of_guesses > 9:
            print("GAME OVER")
else:
    print("Error: You enter invalid number.")
