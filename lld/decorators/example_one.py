"""
using the decorators in the python

python decorators are juist a way to pass a function inside a function 


https://realpython.com/primer-on-python-decorators/

"""

def my_decorator(func):
    """
    This is decorator function
    """

    print("This is first print")

    func()

    print("This is the second print")


@my_decorator
def test():

    print("This is the midde")




