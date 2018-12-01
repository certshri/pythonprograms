def addition(number1, number2):
        print("\nSum of two numbers", number1+number2)
        return
def multiplication(number1, number2):
        print("\n multipilcation of two numbers is ", number1*number2)
        return
def subtraction(number1,number2):
        print("\nSubtraction of two numbers is", number1-number2)
        return
def division(number1, number2):
        print("\nDivision of two numbers is", number1/number2)
        return
def menu_choice():
    check = 1
    while check == 1:
     menu =int(input("\nEnter your menu choice\n1 for addition\n2 for Subtraction\n"
                      "3 for Multiplication\n4 for Division\n"))
     if menu > 0 and menu < 5:
      check = 2
     else:
         print("\n invalid menu choice \n")
    return menu
def Input_numbers():
    number1 = int(input("\nEnter 1st Number\n"))
    number2 = int(input("\nEnter 2nd Number\n"))
    return number1, number2
def operation():
    menu = menu_choice()
    if menu == 1:
        addition(Input_numbers())
    if menu == 2 :
        subtraction()
    if menu == 3:
        multiplication()
    if menu == 4:
        division()
    return

repeat = 'yes'
while repeat == 'yes':
 menu_choice()
 Input_numbers()
 operation()
 print("\nWould you like to repeat\n")
 repeat = input()



