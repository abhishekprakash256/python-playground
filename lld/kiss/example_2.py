"""
The example for the oops principle 


Tips

To maintain simplicity in code, it’s important to follow some practical tips.

Firstly, avoid over-engineering and excessive abstractions. Look for simple and straightforward solutions that meet specific needs without adding unnecessary complexity. Also, avoid code repetition and duplication, in line with the DRY principle. By grouping common functionalities and avoiding redundancies, you keep the code clearer and more concise.

Additionally, it’s important to keep variable, function, and class names clear and explicit. Well-chosen names facilitate code understanding and reduce the need for additional comments. Also, avoid premature optimizations and unnecessary complex features. Focus on solving specific problems and add additional features only when truly necessary.
In Practice

Let’s take a concrete example to illustrate the application of the KISS principle. Suppose we are developing a simple calculator program. Instead of creating a complex structure with sophisticated classes and interfaces, we can opt for a simple solution using direct functions or methods to perform basic operations such as addition, subtraction, multiplication, and division. This would make the code clearer, easier to understand, and easier to maintain.

By applying the KISS principle, we prioritize simplicity and clarity in the code, which facilitates understanding, maintenance, and problem-solving, while promoting software flexibility and scalability.
"""

class Shape():

    def area(self):

        pass

class Sqaure(Shape):

    def __init__(self,side):

        self.side = side
    
    def area(self):

        return self.side * self.side
    

class Circle(Shape):

    def __init__(self,radius):

        self.radius = radius

    def area(self):

        return 3.145 * self.radius ** 2


dummy_circle = Circle(5)

print(dummy_circle.area())