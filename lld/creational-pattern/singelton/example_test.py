"""
This is the test example 
"""

class Logger():

    instances_mappper = {}

    #the new keyword with underscore is imp
    def __new__(cls):

        if cls not in cls.instances_mappper :

            print("Creating the new Logger instance")

            cls.instances_mappper[cls] = super().__new__(cls)

        return cls.instances_mappper[cls]


logger1 = Logger()
logger2 = Logger()


#print(logger1.__instance)

if logger1 is logger2 :

    print("The logger is same")

else :

    print("The logger is not same")

