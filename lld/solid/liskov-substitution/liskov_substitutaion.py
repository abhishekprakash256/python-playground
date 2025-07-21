"""
The file to experimnet for the liskov substution

https://www.youtube.com/watch?v=ZSAXFDNPcIg&ab_channel=Codingw%2FdaBest


"""

"""
The example for the correct --> 

so we make a super class that can have the methods and then the new methods can be applied to sub classes 

if we create an class name KichenAppliance and that has the method like open , close and set_temp and we create the other applicance that can not has the methdo we have to 

make the class that can make the seperate class for them

"""

class KitchenAppliance:

    def turn_on(self):
        print("The appliance is turned on")
        return True

    def turn_off(self):
        print("The appliance is turned off")
        return True


class KitchenApplianceTempr(KitchenAppliance):

    def set_tempr(self, tempr):
        print(f"The temperature is set to {tempr}")
        return True


class Toaster(KitchenApplianceTempr):
    pass


class Blender(KitchenAppliance):
    pass


# Testing
dummy_blender = Blender()
dummy_blender.turn_on()

dummy_toaster = Toaster()
dummy_toaster.turn_on()
dummy_toaster.set_tempr(100)