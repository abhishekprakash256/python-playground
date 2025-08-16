"""
The borg principle to make the singleton class
"""

class Borg():

    _shared_state = {}

    def __init__(self):

        self.__dict__ = self._shared_state



class Logger(Borg):

    def __init__(self):

        super().__init__()
        
        if not hasattr(self, "message"):

            self.message = []

    def log(self, msg):

        self.message.append(msg)    

        print(f"The message is {msg}")



logger1 = Logger()

logger2 = Logger()

logger1.log("one")

logger2.log("two")

if logger1 is logger2 :

    print("The logger is same")

else :

    print("The logger is not same")

print(logger1.message is logger2.message)  # True (shared state)