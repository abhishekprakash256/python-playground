"""
using the decorator 
"""

def singleton(cls):

    instance_mapper = {}

    def get_instance(*args, **kwargs):

        if cls not in instance_mapper :

            print("The instance has been created")

            instance_mapper[cls] = cls(*args , **kwargs)

        return instance_mapper[cls]

    return get_instance


@singleton
class Logger():

    def log(self,message):

        print(f"This is the message {message}")

        return True
    
logger1 = Logger()
logger2 = Logger()

if logger1 is logger2:

    print("Instance is Same")

else:

    print("Instance is not Same")