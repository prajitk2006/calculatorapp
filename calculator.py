print("Hello, Welcome to the Calculator Program!")
n = int(input("Enter number of times you want to use the calculator: "))
for i in range(n) :
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", a + b)
    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", a - b)
    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result: ", a * b)
    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result: ", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 5:
        print("Exiting the calculator. Goodbye!")
    else :
        print("Invalid choice! Please try again.")