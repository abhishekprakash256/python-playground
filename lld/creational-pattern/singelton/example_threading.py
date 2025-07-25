"""
The example of the thred lock using the threading lock for singleton isntance 
"""

import threading 

class Logger():

    __instance = None 
    __lock = threading.Lock()


    def __new__(cls):

        with cls.__lock :

            if cls.__instance is None :

                print("Creating the new thread safe lock")

                cls.__instance = super().__new__(cls)

            return cls.__instance
        
    def log(self, msg) :

        print(f"The message is {msg}")

        return True
    

#make the logger 

logger1 = Logger()

logger2 = Logger()


if logger1 is logger2:

    print("The instance is same")

else:

    print("The instance is not same")