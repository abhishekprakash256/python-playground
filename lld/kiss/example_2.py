"""
The example for the oops principle 
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