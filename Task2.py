print("Calculator")

num1= float(input("Enter number 1 here: "))
num2= float(input("Enter number 2 here: "))

print("\nPress 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division")

choice = int(input("Choose 1 to 4 :"))

if choice == 1:
    print("The Addition is =", num1+num2)

elif choice == 2:
    print("The Subtraction is =", num1-num2)

elif choice == 3:
    print("The Multiplication is =", num1*num2)

elif choice == 4:
    print("The Division is =", num1//num2)

else:
    print("Invalid input")











