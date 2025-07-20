"""
The file to make the open close example 
"""

class MakeUser():

    def __init__(self, name, title, salary ):

        self.__name = name
        self.__title = title
        self.__salary = salary

    
    def get_name(self):

        return f"The user name -> {self.__name} "
    
    def get_salary(self):

        return f"The salary of the user -> {self.__salary}"
    
    def get_title(self):

        return f"The title of the user -> {self.__title}"
    


#Store the data in dict 
mapper = {}

#the value store in the dict
mapper[1] = MakeUser("Abhi", "SDE" , 100)
mapper[2] = MakeUser("Anny", "AE" , 100)
mapper[3] = MakeUser("Tom", "SDE" , 100)
mapper[4] = MakeUser("Cat", "SDE" , 100)
mapper[5] = MakeUser("Dan", "SDE" , 100)


print(mapper[1].get_name())
print(mapper[2].get_name())



class MakeUserModify():
    """
    The make user has been modified to get more data , whichh is not good approach
    """

    def __init__(self, performance):

        self.__performance = performance

    def get_experience(self):

        return f"get the performance {self.__performance} "
    

class Performance(MakeUser):

    def __init__(self,performance) :

        self.__performance = performance

    def get_performance(self):

        return f"The performance of the user--> {self.__performance}"



mapper[1] = Performance("A") 

print(mapper[1].get_performance())


