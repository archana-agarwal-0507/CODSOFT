import random
#All the choices in the game
Choices=["rock","paper","scissors"]
while True:
#Taking user input
    user=input("Enter your choice. Rock/Paper/Scissors: ").lower()
#Taking random input from computer
    computer=random.choice(Choices)
    if user not in Choices:
        print("Invalid input")
    else:
        print("computer choice:",computer)
        if user==computer:
            print("It's a tie!")
        elif(user=="rock" and computer=="scissors")or(user=="paper" and computer=="rock")or(user=="scissors" and computer=="paper"):
            print("You win!")
        else:
            print("You lose!")
#Play again- yes or no
    play_again=input("Play again? yes/no? ").lower()
    if play_again=="yes":
        print("Good luck!")
    else:
        print("Have a nice day!")
        break
