# Import math module for scientific operations
import math


print("Welcome to the Scientific Calculator")


# Store previous calculations
history = []


# ---------------- Basic Operations ----------------

def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    # Avoid division by zero
    if num2 == 0:
        return None

    return num1 / num2



# ---------------- Scientific Operations ----------------

def square_root(num):
    # Negative numbers are not valid for normal square root
    if num < 0:
        return None

    return math.sqrt(num)


def power(num1, num2):
    return math.pow(num1, num2)


def sine(num):
    # Convert degrees to radians because math.sin uses radians
    return math.sin(math.radians(num))


def cosine(num):
    return math.cos(math.radians(num))


def tangent(num):
    return math.tan(math.radians(num))


def cotangent(num):
    # cot(x) = 1 / tan(x)
    value = math.tan(math.radians(num))

    if value == 0:
        return None

    return 1 / value



# ---------------- Main Program ----------------

while True:

    operation = input(
        "\nEnter operation (+, -, *, /, sqrt, pow, sin, cos, tan, cot): "
    ).lower()


    try:

        # Operations that need one number
        if operation in ["sqrt", "sin", "cos", "tan", "cot"]:

            num = float(input("Enter a number: "))


        # Operations that need two numbers
        elif operation in ["+", "-", "*", "/", "pow"]:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))


        else:
            print("Invalid operation")
            continue



        # Select operation

        if operation == "+":
            result = addition(num1, num2)


        elif operation == "-":
            result = subtraction(num1, num2)


        elif operation == "*":
            result = multiplication(num1, num2)


        elif operation == "/":

            result = division(num1, num2)

            if result is None:
                print("Cannot divide by zero")
                continue


        elif operation == "pow":
            result = power(num1, num2)


        elif operation == "sqrt":

            result = square_root(num)

            if result is None:
                print("Cannot calculate square root of a negative number")
                continue


        elif operation == "sin":
            result = sine(num)


        elif operation == "cos":
            result = cosine(num)


        elif operation == "tan":
            result = tangent(num)


        elif operation == "cot":

            result = cotangent(num)

            if result is None:
                print("Cotangent is undefined for this value")
                continue



        # Display result

        print("Your result is:", result)



        # Save calculation in history

        if operation in ["sqrt", "sin", "cos", "tan", "cot"]:

            history.append(
                f"{operation}({num}) = {result}"
            )

        else:

            history.append(
                f"{num1} {operation} {num2} = {result}"
            )



        # Show history

        show_history = input(
            "Do you want to see calculation history? (y/n): "
        )


        if show_history.lower() == "y":

            print("\nCalculation History:")

            for item in history:
                print(item)



    except ValueError:

        print("Invalid input! Please enter numbers only.")



    # Continue program

    again = input(
        "\nDo you want to continue? (y/n): "
    )


    if again.lower() != "y":
        break



print("Calculator closed")
