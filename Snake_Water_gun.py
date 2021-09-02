import random

chance = 0
user = 0
computer = 0
draw = 0
print("Welcome You have 10 chance\n Press s for Snake\n Press w for Water\n Press g for Gun")

while chance < 10:
    lst = ["Snake", "Water", "Gun"]
    rand = str(random.choice(lst))
    cho = str(input("\nEnter your choice : "))
    if cho == "s" and rand == "Snake" or cho == "w" and rand == "Water" or cho == "g" and rand == "Gun":
        print("Game draw!!!")
        draw = draw + 1
        print("Computer choose ", rand)
        chance = chance + 1

    elif cho == "s" and rand == "Water" or cho == "w" and rand == "Gun" or cho == "g" and rand == "Snake":
        print("You won!!!")
        user = user + 1
        print("Computer choose ", rand)
        chance = chance + 1

    elif cho == "s" and rand == "Gun" or cho == "w" and rand == "Snake" or cho == "g" and rand == "Water":
        print("Sorry You lose!!!")
        computer = computer + 1
        print("Computer choose ", rand)
        chance = chance + 1

    else:
        print("Error: You entered invalid option please Enter valid option")

string = f"\n\n You won {user} times\n Computer won {computer} times\n Game Draw {draw} times"
print(string)
if user > computer:
    print("\nCongratulation!!! CHAMP\nYou are The Winner.")

elif user < computer:
    print("\nSORRY! Better luck next time")

else:
    print("\nOhh GAME DRAW \nTry again")
