from utils import *
while True:
    operation = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()
    if operation == "exit":
        break
    if operation not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute", "exit"]:
        print("Invalid operation!")
        
        continue
    if operation == "absolute":
        num = float(input("Enter a number:\n"))
        result = absolute_value(num)
    else:
        num1 = float(input("Enter the first number:\n"))
        num2 = float(input("Enter the second number:\n"))
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = divide(num1, num2)
        elif operation == "exponent":
            result = exponentiate(num1, num2)
        elif operation == "modulo":
            result = modulus(num1, num2)
        elif operation == "floor_divide":
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = floor_divide(num1, num2)
    print(f"The result is: {result}")
