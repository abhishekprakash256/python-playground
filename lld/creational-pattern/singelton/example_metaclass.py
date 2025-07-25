"""
using the singleton metalcass 
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print("Creating singleton using metaclass")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class MetaLogger(metaclass=SingletonMeta):
    def log(self, msg):
        print(f"[MetaLog]: {msg}")


logger1 = MetaLogger()
logger2 = MetaLogger()

print(logger1 is logger2)  # True
