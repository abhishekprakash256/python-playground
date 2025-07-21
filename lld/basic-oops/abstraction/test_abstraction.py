"""
example of the abstraction method
"""

from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass  # Abstract method - no implementation

    def sleep(self):
        print("Sleeping...")  # Concrete method

# Concrete Subclass
class Dog(Animal):
    def speak(self):
        print("Woof!")

# Another Concrete Subclass
class Cat(Animal):
    def speak(self):
        print("Meow!")

# Usage
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
    animal.sleep()
