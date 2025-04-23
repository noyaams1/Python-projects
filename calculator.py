import operator
import math

# Define supported operations including square root
operations = ['+', '-', '*', '/', '//', '%', '**', 'sqrt']

def calculator(num1, num2, math_operation):
    # Validate if operation is supported
    if math_operation not in operations:
        print("Invalid arithmetic operation!")
        return None

    # Division by zero check (only for operations that use num2)
    if math_operation in ['/', '//', '%'] and num2 == 0:
        print("ZeroDivisionError")
        return None

    # Perform the operation
    if math_operation == '+':
        result = operator.add(num1, num2)
    elif math_operation == '-':
        result = operator.sub(num1, num2)
    elif math_operation == '*':
        result = operator.mul(num1, num2)
    elif math_operation == '/':
        result = operator.truediv(num1, num2)
    elif math_operation == '//':
        result = operator.floordiv(num1, num2)
    elif math_operation == '%':
        result = operator.mod(num1, num2)
    elif math_operation == '**':
        result = operator.pow(num1, num2)
    elif math_operation == 'sqrt':
        # Only use num1 for square root
        if num1 < 0:
            print("MathError: Cannot take square root of a negative number.")
            return None
        result = math.sqrt(num1)

    # Round result to 2 decimal places and return
    return round(result, 2)

# Get input from user
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
math_operation = input("Enter an operator (+, -, *, /, //, %, **, sqrt): ")

# Print result
print(calculator(num1, num2, math_operation))

# --------------------------------------------
# RELIABILITY:
# - Checks for invalid operations and division by zero.
# - Handles square root of negative numbers.
# - Uses built-in operator functions for consistency.

# MAINTAINABILITY:
# - All operations are in a single function, easy to update or extend.
# - Readable structure with one condition per block.
# - Adding or modifying an operation is straightforward.

# SCALABILITY:
# - Adding more than 2 numbers and more operations is easy.
# - Future CLI or GUI interfaces can reuse the same function.
# - Easy to adapt for batch processing or expression parsing.
