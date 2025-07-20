"""
The inheritance is taking the methods from the top class 
"""

class Vehicle():

    def __init__(self,color, weight = 0 ):

        self.color = color
        self.weight = weight

    def get_color(self):

        return self.color
    
    def get_weight(self):

        return self.weight
    


class Car(Vehicle):

    def __init__(self,speed , accleration,color):

        self.speed = speed
        self.accleration = accleration

        #pass the inherited class
        super().__init__(color)


    def get_speed(self):

        return self.speed
    
    def get_accleration(self):

        return self.accleration
    


#make the car
test_car = Car(40,30,"red")

print(test_car.get_color())

print(test_car.get_speed())

print(test_car.get_weight())
