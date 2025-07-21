"""
Clients should not be forced to depend on methods that they do not use.

A class should only have the methods that can be used in client , if the methods are not used they go to waste 

"""

class Shape():

    def area(self,dim):

        print(f"The area is {dim}")

        return True
    
    def perimeter(self,dim):

        print(f"The perimeter is {dim}")

    def surfacearea(self,dim):

        print(f"The surface area is {dim}")

    def volume(self,dim):

        print(f"The surface area is {dim}")



test_square = Shape() #doesn't have the volume and sureface area

test_cube = Shape()  #doesn't have the permimeter and ara



#the best approach is to make seperate class for the 2d and 3d shape 

class TwoDimShape():

    def area(self,dim):

        print(f"The area is {dim}")

        return True
    
    def perimeter(self,dim):

        print(f"The perimeter is {dim}")


class ThreeDimShape():

    def surfacearea(self,dim):

        print(f"The surface area is {dim}")

    def volume(self,dim):

        print(f"The surface area is {dim}")


test_square_2d = TwoDimShape()

test_cube_3d = ThreeDimShape()
       