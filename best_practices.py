"""
This module demonstrates Python best practices and common pitfalls to avoid.

It covers the following topics:
1. Code Style (PEP 8)
2. Naming Conventions
3. Error Handling
4. Code Organization
5. Performance Tips

Each section includes examples of good and bad practices.
"""

import time
from typing import List, Dict


# 1. Code Style (PEP 8)
def demonstrate_code_style():
    """Demonstrate good and bad code style practices."""
    # Good: Use 4 spaces for indentation
    def good_indentation():
        return "Properly indented"

    # Bad: Using tabs or inconsistent indentation
    def bad_indentation():
	    return "Improperly indented"

    # Good: Limit lines to 79 characters
    long_string = ("This is a long string that we don't want to extend beyond "
                   "79 characters, so we split it across lines.")

    # Bad: Lines extending beyond 79 characters
    bad_long_string = "This is a long string that extends beyond 79 characters and makes the code harder to read."

    # Good: Use spaces around operators
    x = 5 + 3

    # Bad: No spaces around operators
    y=5+3


# 2. Naming Conventions
class GoodClassName:
    """A class demonstrating good naming conventions."""

    def __init__(self):
        self.instance_variable = 42

    def method_name(self):
        """A method with a good name."""
        local_variable = 10
        return local_variable

class badclassname:
    """A class demonstrating bad naming conventions."""

    def __init__(self):
        self.InstanceVariable = 42

    def MethodName(self):
        """A method with a bad name."""
        LocalVariable = 10
        return LocalVariable


# 3. Error Handling
def demonstrate_error_handling():
    """Demonstrate good and bad error handling practices."""
    # Good: Specific exception handling
    try:
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")

    # Bad: Bare except clause
    try:
        result = 10 / 0
    except:
        print("An error occurred.")

    # Good: Using else clause
    try:
        value = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        print(f"You entered: {value}")

    # Good: Using finally for cleanup
    lock = None
    try:
        lock = acquire_lock()
        # Perform operations
    finally:
        if lock:
            release_lock(lock)


# 4. Code Organization
# Good: Group related functions and classes
class Shape:
    """A base class for shapes."""
    pass

class Circle(Shape):
    """A circle shape."""
    pass

class Square(Shape):
    """A square shape."""
    pass

def calculate_area(shape: Shape) -> float:
    """Calculate the area of a shape."""
    pass

# Bad: Mixing unrelated functions and classes
def unrelated_function():
    """An unrelated function."""
    pass


# 5. Performance Tips
def demonstrate_performance_tips():
    """Demonstrate good and bad performance practices."""
    # Good: Use list comprehension for simple loops
    squares = [x**2 for x in range(10)]

    # Bad: Using a loop for the same operation
    squares_bad = []
    for x in range(10):
        squares_bad.append(x**2)

    # Good: Use join for string concatenation
    words = ["Hello", "world", "!"]
    sentence = " ".join(words)

    # Bad: Using + for string concatenation in a loop
    sentence_bad = ""
    for word in words:
        sentence_bad += word + " "
    sentence_bad = sentence_bad.strip()

    # Good: Use generator for large datasets
    def number_generator(n):
        for i in range(n):
            yield i

    # Bad: Creating a large list in memory
    def number_list(n):
        return list(range(n))


def main():
    """Main function to demonstrate best practices."""
    demonstrate_code_style()
    demonstrate_error_handling()
    demonstrate_performance_tips()


if __name__ == "__main__":
    main()