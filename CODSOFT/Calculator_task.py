#This is a calculator program for simple arithmetic operations

#Taking input of first number
num1=float(input("enter first number:"))
#Taking input of second number
num2=float(input("enter second number:"))
#choosing an operation to do 
operation=input("select your choice of operation. \nAddition\nSubtraction\nMultiplication\nDivision\n").lower()
match operation:
    case "addition":
        result=num1+num2
    case "subtraction":
        result=num1-num2
    case "multiplication":
        result=num1*num2
    case "division":
        if(num2==0):
           print("cant define")
        else:
            result=num1/num2
    case _:
           print("INVALID INPUT")
#printing the result
print(f"{num1} {operation} {num2} = {result}")
