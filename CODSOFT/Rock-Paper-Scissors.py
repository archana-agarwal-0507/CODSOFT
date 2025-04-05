import random
#All the choices in the game
Choices=["rock","paper","scissors"]
name=input("Enter your name: ").lower()
user_score=computer_score=0
while True:
#Taking user input
    user=input("Enter your choice from below options- \nRock\nPaper\nScissors\n").lower()
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
            user_score=user_score+1
        else:
            print("You lose!")
            computer_score=computer_score+1
    print(f"{name}'s score={user_score} and computer's score={computer_score}")
#Play again- yes or no
    play_again=input("Play again? yes/no? ").lower()
    if play_again=="yes":
        print("Good luck!")
    else:
        print("Have a nice day!")
        break
