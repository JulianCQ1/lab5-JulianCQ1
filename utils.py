# FREEZE CODE BEGIN
def greet(name):
    """
    Return a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting in the format "Hello, <name>!".
    """
    return f"Hello, {name}!"


def flip(input_string):
    """
    Reverse the characters in the given string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return input_string[::-1]


def count_letters(input_string, letter):
    """
    Count how many times a specific letter appears in a string.

    Args:
        input_string (str): The string to search.
        letter (str): The letter to count (should be a single character).

    Returns:
        int: The number of occurrences of the letter in the string.
    """
    count = 0
    for char in input_string:
        if char == letter:
            count += 1
    return count

if __name__ == "__main__":
  print("This file is being run directly.")
# FREEZE CODE END
def add(num1, num2):
    """
    Return the sum of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The sum of num1 and num2.
    """
    return num1 + num2
def subtract(num1, num2):
    """
    Return the difference of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The difference of num1 and num2.
    """
    return num1 - num2
def multiply(num1, num2):
    """
    Return the product of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The product of num1 and num2.
    """
    return num1 * num2
def divide(num1, num2):
    """
    Return the quotient of two numbers.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        float: The quotient of num1 and num2.
    """
    return num1 / num2
def exponentiate(num1, num2):
    """
    Return num1 raised to the power of num2.

    Args:
        num1 (int): The base number.
        num2 (int): The exponent.

    Returns:
        int: The result of num1 raised to the power of num2.
    """
    return num1 ** num2
def modulus(num1, num2):
    if num2 == 0:
        return "Error: Modulo by zero is not allowed."
    """
    Return the remainder of num1 divided by num2.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The remainder of num1 divided by num2.
    """
    return num1 % num2
def floor_divide(num1, num2):
    if num2 == 0:
        return "Error: Floor division by zero is not allowed."
    """
    Return the floor division of num1 by num2.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.

    Returns:
        int: The floor division of num1 by num2.
    """
    return num1 // num2
def absolute_value(num):
    """
    Return the absolute value of a number.

    Args:
        num (int): The number to find the absolute value of.

    Returns:
        int: The absolute value of num.
    """
    return abs(num)
