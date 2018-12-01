
def addition(number1,number2):
    return number1+number2
def subtraction(number1,number2):
    return number1-number2
def multiplication(number1,number2):
    return number1*number2
def division(number1,number2):
    return number1/number2
repeat = 'yes'
while repeat == 'yes':
 print("Hello, what would you like to do")
 check = 0
 while check == 0:

        operation = int(input("Enter 1for Addition\nEnter 2 for Subtraction\n"
                              "Enter 3 for Multiplication\nEnter 4 for Division\n"))
        if 0 < operation and operation < 5:
            check = 1
        else:
                print("Wrong input Please enter as per menu\n")

  number1 = int(input("Enter first number\n"))
  number2 = int(input("Enter second number\n"))

if operation == 1:
    print("\nAddition of two numbers is", addition(number1,number2))
elif operation == 2:
    print("\nSubtraction of two numbers is", subtraction(number1,number2))
elif operation == 3:
    print("\n Multiplication of two numbers is", multiplication(number1, number2))
elif operation == 4:
    if number2 == 0:
        print("division not defined")
    else:
        print("Division of two numbers is", division(number1, number2))
print("\n would you like to repeat, Enter yes or no")
repeat = input()
if repeat == 'no'
break