"""
This module demonstrates Python functions and modules.

It covers function definition, parameters, return values, lambda functions,
and how to work with modules.
"""

import math
import random as rnd
from datetime import datetime


def greet(name):
    """
    A simple function that greets a person.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width


def demonstrate_default_parameters(name="World"):
    """
    Demonstrate the use of default parameters.

    Args:
        name (str, optional): The name to greet. Defaults to "World".

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def demonstrate_args(*args):
    """
    Demonstrate the use of *args for variable-length arguments.

    Args:
        *args: Variable number of arguments.

    Returns:
        str: A string representation of all arguments.
    """
    return f"You passed the following arguments: {args}"


def demonstrate_kwargs(**kwargs):
    """
    Demonstrate the use of **kwargs for keyword arguments.

    Args:
        **kwargs: Keyword arguments.

    Returns:
        str: A string representation of all keyword arguments.
    """
    return f"You passed the following keyword arguments: {kwargs}"


# Lambda function example
square = lambda x: x**2


def demonstrate_functions():
    """Demonstrate various aspects of Python functions."""
    print("1. Basic function call:")
    print(greet("Alice"))

    print("\n2. Function with multiple parameters:")
    print(f"The area of a 5x3 rectangle is: {calculate_rectangle_area(5, 3)}")

    print("\n3. Function with default parameters:")
    print(demonstrate_default_parameters())
    print(demonstrate_default_parameters("Bob"))

    print("\n4. Function with *args:")
    print(demonstrate_args(1, 2, 3, "four", [5, 6]))

    print("\n5. Function with **kwargs:")
    print(demonstrate_kwargs(name="Charlie", age=30, city="New York"))

    print("\n6. Lambda function:")
    print(f"The square of 7 is: {square(7)}")


def demonstrate_modules():
    """Demonstrate the use of modules and imports."""
    print("\nDemonstrating modules:")
    
    print("1. Using the 'math' module:")
    print(f"The square root of 16 is: {math.sqrt(16)}")
    print(f"The value of pi is approximately: {math.pi:.4f}")

    print("\n2. Using the 'random' module (imported as 'rnd'):")
    print(f"A random number between 1 and 10: {rnd.randint(1, 10)}")

    print("\n3. Using a specific function from the 'datetime' module:")
    print(f"The current date and time is: {datetime.now()}")


def main():
    """Main function to demonstrate functions and modules."""
    print("Demonstrating Python Functions:")
    demonstrate_functions()

    print("\nDemonstrating Python Modules:")
    demonstrate_modules()


if __name__ == "__main__":
    main()