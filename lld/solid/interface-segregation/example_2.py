"""
The example of the interface segregation
"""

from abc import ABC, abstractmethod

# Interface for 2D shapes
class TwoDimensionalShape(ABC):

    @abstractmethod
    def area(self, dim):
        pass

    @abstractmethod
    def perimeter(self, dim):
        pass


# Interface for 3D shapes
class ThreeDimensionalShape(ABC):

    @abstractmethod
    def surface_area(self, dim):
        pass

    @abstractmethod
    def volume(self, dim):
        pass


class Square(TwoDimensionalShape):

    def area(self, side):
        return side * side

    def perimeter(self, side):
        return 4 * side


class Cube(ThreeDimensionalShape):

    def surface_area(self, side):
        return 6 * side * side

    def volume(self, side):
        return side ** 3


sq = Square()
print("Square Area:", sq.area(4))
print("Square Perimeter:", sq.perimeter(4))

cb = Cube()
print("Cube Surface Area:", cb.surface_area(4))
print("Cube Volume:", cb.volume(4))
