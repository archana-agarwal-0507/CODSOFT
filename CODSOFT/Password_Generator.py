import random
import string
password=""
#Taking user input for the length of the password
length=int(input("Enter the length of your password: "))
#Storing all the possible characters a password can have in Characters variable
characters= string.ascii_letters + string.digits + string.punctuation
#logic
while len(password)<=length:
    password=password+random.choice(characters)
print("GENERATED PASSWORD:",password)
                         
