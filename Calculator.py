# Ask for user input
number1 = float(input("Enter your Number 1: "))
number2 = float(input("Enter your Number 2: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == '+':
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == '-':
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == '*':
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of (+, -, *, /).")
