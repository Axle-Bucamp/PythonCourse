"""
This module demonstrates Pythonic class design in Python.

It covers:
- Class definition
- Instance methods
- Class methods
- Static methods
- Properties
- Magic methods
- Inheritance
- Composition

Each concept is explained with comments and demonstrated with code examples.
"""

from abc import ABC, abstractmethod


class Animal:
    """
    A base class representing an animal.

    This class demonstrates basic class structure, class and instance attributes,
    and various types of methods.
    """

    # Class attribute
    kingdom = "Animalia"

    def __init__(self, name, age):
        """
        Initialize an Animal instance.

        Args:
            name (str): The name of the animal.
            age (int): The age of the animal.
        """
        self.name = name  # Instance attribute
        self._age = age  # Protected instance attribute

    def make_sound(self):
        """An instance method that needs to be implemented by subclasses."""
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """
        A class method to create an Animal instance using birth year instead of age.

        Args:
            name (str): The name of the animal.
            birth_year (int): The birth year of the animal.

        Returns:
            Animal: An instance of the Animal class.
        """
        from datetime import datetime
        age = datetime.now().year - birth_year
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        """
        A static method to check if an age represents an adult.

        Args:
            age (int): The age to check.

        Returns:
            bool: True if the age represents an adult, False otherwise.
        """
        return age >= 18

    @property
    def age(self):
        """Property to get the age of the animal."""
        return self._age

    @age.setter
    def age(self, value):
        """Setter for the age property with validation."""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def __str__(self):
        """Magic method for string representation of the object."""
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        """Magic method for the official string representation of the object."""
        return f"Animal(name='{self.name}', age={self.age})"


class Dog(Animal):
    """
    A Dog class inheriting from Animal.

    This class demonstrates inheritance and method overriding.
    """

    def __init__(self, name, age, breed):
        """
        Initialize a Dog instance.

        Args:
            name (str): The name of the dog.
            age (int): The age of the dog.
            breed (str): The breed of the dog.
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        """Override the make_sound method from the parent class."""
        return "Woof!"


class Cat(Animal):
    """
    A Cat class inheriting from Animal.

    This class demonstrates multiple inheritance and the use of abstract base classes.
    """

    def make_sound(self):
        """Override the make_sound method from the parent class."""
        return "Meow!"


class Pet(ABC):
    """
    An abstract base class for pets.

    This class demonstrates the use of abstract methods and multiple inheritance.
    """

    @abstractmethod
    def play(self):
        """An abstract method that must be implemented by subclasses."""
        pass


class HouseCat(Cat, Pet):
    """
    A HouseCat class inheriting from both Cat and Pet.

    This class demonstrates multiple inheritance and method implementation.
    """

    def play(self):
        """Implement the play method from the Pet abstract base class."""
        return f"{self.name} is playing with a ball of yarn."


class Shelter:
    """
    A Shelter class demonstrating composition.

    This class has a collection of Animal objects, showing how classes can be composed
    of other classes.
    """

    def __init__(self):
        """Initialize an empty shelter."""
        self.animals = []

    def add_animal(self, animal):
        """
        Add an animal to the shelter.

        Args:
            animal (Animal): The animal to add to the shelter.
        """
        self.animals.append(animal)

    def list_animals(self):
        """List all animals in the shelter."""
        return [str(animal) for animal in self.animals]


def main():
    """Demonstrate the usage of the classes defined in this module."""
    # Demonstrating basic class usage
    dog = Dog("Buddy", 5, "Golden Retriever")
    print(dog)  # Using __str__ method
    print(dog.make_sound())

    # Demonstrating class method
    cat = Cat.from_birth_year("Whiskers", 2018)
    print(cat)

    # Demonstrating static method
    print(f"Is the cat an adult? {Animal.is_adult(cat.age)}")

    # Demonstrating property usage
    try:
        cat.age = -1  # This will raise a ValueError
    except ValueError as e:
        print(f"Error setting age: {e}")

    cat.age = 4  # This will work
    print(f"Updated cat's age: {cat.age}")

    # Demonstrating multiple inheritance
    house_cat = HouseCat("Smokey", 3)
    print(house_cat.play())

    # Demonstrating composition
    shelter = Shelter()
    shelter.add_animal(dog)
    shelter.add_animal(cat)
    shelter.add_animal(house_cat)

    print("Animals in the shelter:")
    for animal in shelter.list_animals():
        print(animal)


if __name__ == "__main__":
    main()