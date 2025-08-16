"""
The file to implement the decorator 
"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def compute():
    time.sleep(1)
    print("Done computing")

compute()




