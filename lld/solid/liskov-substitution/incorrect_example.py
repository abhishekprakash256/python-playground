"""
An incorrect exmple of the liskov priciple 
When a child Class cannot perform the same actions as its parent Class, this can cause bugs.

If you have a Class and create another Class from it, it becomes a parent and the new Class becomes a child. The child Class should be able to do everything the parent Class can do. This process is called Inheritance.

The child Class should be able to process the same requests and deliver the same result as the parent Class or it could deliver a result that is of the same type


the down example we have a prent class as kitchen applicance that can turn on , turn off and set tempr in the applicance , but all the appliance can set the tempr , they can have differenent functions
"""

class KitchenAppliance():

    def turn_on(self):

        print("The applicance is turned on")

        return True
    
    def turn_off(self):

        print("The appliance is turned off")

        return False
    
    def set_tempr(self,tempr):

        print(f"The tempr is not {tempr}")
    

class Toaster(KitchenAppliance):

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()
    
    def set_tempr(self, tempr):
        return super().set_tempr(tempr)
    

class AirFryer(KitchenAppliance):

    def turn_off(self):
        return super().turn_off()
    
    def turn_on(self):
        return super().turn_on()
    
    def set_tempr(self, tempr):
        return super().set_tempr(tempr)


class Blender(KitchenAppliance):
    """
    The blender can not have the method of the set tempr that violates the liskov principle
    """

    def turn_on(self):
        return super().turn_on()
    
    def turn_off(self):
        return super().turn_off()
    



