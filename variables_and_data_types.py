"""
Variables and Data Types in Python

This module demonstrates the basic data types in Python and how to work with variables.
It covers integers, floats, strings, booleans, lists, tuples, and dictionaries.

Each data type is explained with comments and demonstrated with code examples.
"""

def main():
    """
    Main function to demonstrate various data types in Python.
    """
    print("Welcome to the Python Variables and Data Types tutorial!")
    
    # Integers (int)
    # Integers are whole numbers, positive or negative, without decimals.
    age = 30
    year = 2023
    print(f"\nIntegers (int):\nAge: {age}, Year: {year}")
    print(f"Type of 'age': {type(age)}")

    # Floats (float)
    # Floats are numbers with decimal points.
    pi = 3.14159
    temperature = -0.5
    print(f"\nFloats (float):\nPi: {pi}, Temperature: {temperature}°C")
    print(f"Type of 'pi': {type(pi)}")

    # Strings (str)
    # Strings are sequences of characters, enclosed in single or double quotes.
    name = "Alice"
    greeting = 'Hello, World!'
    print(f"\nStrings (str):\nName: {name}, Greeting: {greeting}")
    print(f"Type of 'name': {type(name)}")

    # Booleans (bool)
    # Booleans represent True or False values.
    is_python_fun = True
    is_difficult = False
    print(f"\nBooleans (bool):\nIs Python fun? {is_python_fun}, Is it difficult? {is_difficult}")
    print(f"Type of 'is_python_fun': {type(is_python_fun)}")

    # Lists
    # Lists are ordered, mutable collections of items, which can be of different types.
    fruits = ["apple", "banana", "cherry"]
    mixed_list = [1, "two", 3.0, True]
    print(f"\nLists:\nFruits: {fruits}, Mixed list: {mixed_list}")
    print(f"Type of 'fruits': {type(fruits)}")

    # Tuples
    # Tuples are ordered, immutable collections of items, which can be of different types.
    coordinates = (10, 20)
    rgb_color = (255, 0, 128)
    print(f"\nTuples:\nCoordinates: {coordinates}, RGB Color: {rgb_color}")
    print(f"Type of 'coordinates': {type(coordinates)}")

    # Dictionaries (dict)
    # Dictionaries are unordered collections of key-value pairs.
    person = {
        "name": "Bob",
        "age": 25,
        "city": "New York"
    }
    print(f"\nDictionaries (dict):\nPerson: {person}")
    print(f"Type of 'person': {type(person)}")

    print("\nThank you for learning about Python variables and data types!")

if __name__ == "__main__":
    main()