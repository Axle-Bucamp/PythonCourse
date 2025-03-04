"""
Python Control Structures

This module demonstrates the basic control structures in Python:
1. if-else statements
2. for loops
3. while loops
4. try-except blocks

Each control structure is explained and demonstrated with code examples.
"""

def demonstrate_if_else():
    """Demonstrate if-else statements in Python."""
    print("Demonstrating if-else statements:")
    
    x = 10
    if x > 5:
        print("x is greater than 5")
    elif x == 5:
        print("x is equal to 5")
    else:
        print("x is less than 5")

    # Ternary operator
    result = "positive" if x > 0 else "non-positive"
    print(f"x is {result}")
    print()

def demonstrate_for_loop():
    """Demonstrate for loops in Python."""
    print("Demonstrating for loops:")
    
    # Iterating over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"I like {fruit}")

    # Using range()
    for i in range(3):
        print(f"Count: {i}")

    # Enumerate
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")
    
    print()

def demonstrate_while_loop():
    """Demonstrate while loops in Python."""
    print("Demonstrating while loops:")
    
    count = 0
    while count < 5:
        print(f"Count is {count}")
        count += 1

    # break and continue
    number = 0
    while True:
        if number == 3:
            number += 1
            continue
        if number == 5:
            break
        print(f"Number is {number}")
        number += 1
    
    print()

def demonstrate_try_except():
    """Demonstrate try-except blocks in Python."""
    print("Demonstrating try-except blocks:")
    
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero!")

    try:
        y = int("not a number")
    except ValueError as e:
        print(f"ValueError occurred: {e}")
    finally:
        print("This always executes")
    
    print()

def main():
    """Main function to run all demonstrations."""
    demonstrate_if_else()
    demonstrate_for_loop()
    demonstrate_while_loop()
    demonstrate_try_except()

if __name__ == "__main__":
    main()