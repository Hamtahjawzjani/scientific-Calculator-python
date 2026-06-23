import math
print("Welcome to the calculator")
history = []
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2
def square_root(num):
    if num < 0:
        return None
    return math.sqrt(num)
def power(num1, num2):
    return math.pow(num1, num2)
def sine(num):
    return math.sin(math.radians(num))
def cosine(num):
    return math.cos(math.radians(num))
def tangent(num):
    return math.tan(math.radians(num))
def cotangent(num):
    value = math.tan(math.radians(num))
    if value == 0:
        return None
    return 1 / value
while True:
    operation = input("Enter operation (+, -, *, /, sqrt, pow, sin, cos, tan, cot): ")
    if operation in ["sqrt", "sin", "cos", "tan", "cot"]:
        num = float(input("Enter a number: "))
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    if operation == "+":
        result = addition(num1, num2)
    elif operation == "-":
        result = subtraction(num1, num2)
    elif operation == "*":
        result = multiplication(num1, num2)
    elif operation == "/":
        result = division(num1, num2)
        if result is None:
            print("Cannot divide by zero, try again")
            continue
    elif operation == "sqrt":
        result = square_root(num)
    elif operation == "pow":
        result = power(num1, num2)
    elif operation == "sin":
        result = sine(num)
    elif operation == "cos":
        result = cosine(num)
    elif operation == "tan":
        result = tangent(num)
    elif operation == "cot":
        result = cotangent(num)
    else:
        print("Invalid operation")
        continue
    print("Your result is:", result)
    h = input("Do you want to see calculation history? (y/n): ")
    if operation in ["sqrt", "sin", "cos", "tan", "cot"]:
        history.append(f"{operation}({num}) = {result}")
    else:
        history.append(f"{num1} {operation} {num2} = {result}")
    if h.lower() == "y":
        print("\nHistory:")
        for item in history:
            print(item)
    x = input("Do you want to continue? (y/n): ")
    if x.lower() != "y":
        break
print("Calculator closed")
