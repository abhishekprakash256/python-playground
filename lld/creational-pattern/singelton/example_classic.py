"""
example for creational pattern

simnple definition --

Imagine you have a big toy box that takes a long time to open because its locked with many locks. 
Instead of unlocking it every time you want a toy, the Singleton is like opening it once in the morning and then keeping it 
open all day so you can quickly grab toys whenever you want. It saves you a lot of time!

Singleton Pattern is a creational design pattern that guarantees a class has only one instance and provides a global point of access to it. 

It involves only one class which is responsible for instantiating itself, making sure it creates not more than one instance.

Managing Shared Resources (database connections, thread pools, caches, configuration settings)

Coordinating System-Wide Actions (logging, print spoolers, file managers)

Managing State (user session, application state)

Logger Classes: Many logging frameworks use the Singleton pattern to provide a global logging object. This ensures that log messages are consistently handled and written to the same output stream.

Database Connection Pools: Connection pools help manage and reuse database connections efficiently. A Singleton can ensure that only one pool is created and used throughout the application.

Cache Objects: In-memory caches are often implemented as Singletons to provide a single point of access for cached data across the application.

Thread Pools: Thread pools manage a collection of worker threads. A Singleton ensures that the same pool is used throughout the application, preventing resource overuse.

File System: File systems often use Singleton objects to represent the file system and provide a unified interface for file operations.

Print Spooler: In operating systems, print spoolers manage printing tasks. A single instance coordinates all print jobs to prevent conflicts.



Links -- 

- https://www.geeksforgeeks.org/python/singleton-pattern-in-python-a-complete-guide/

- https://ngcheehou.medium.com/problem-solving-with-the-singleton-design-pattern-a-before-and-after-code-analysis-part-1-42f42156a09c

- https://www.freecodecamp.org/news/singleton-design-pattern-with-javascript/



"""

"""

In python singelton pattern can be implemented using diffent ways , using the new keyword , using the dict , using the import , using the thread locking , using decorator, using metaclass , using borg patttern, uisng the func lru cache tools 


"""



#making the classic way 

class Logger():

    #this name can be changed, this "__" make the instance private as well 
    __instance = None
    

    #the new keyword with underscore is imp
    def __new__(cls):

        if cls.__instance is None :

            print("Creating the new Logger instance")

            cls._instance = super().__new__(cls)

        return cls.__instance
    
    def log(self,message):

        print(f"This is log {message}")

        return True
    


#make the instance of the class 


logger1 = Logger()
logger2 = Logger()

#print(logger1.__instance)

if logger1 is logger2 :

    print("The logger is same")

else :

    print("The logger is not same")





