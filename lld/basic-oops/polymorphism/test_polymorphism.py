"""
The file to test the polymorphism for the class 
"""



class Animal():

    def speak(self):

        return "Sound"
    


class Dog(Animal):

    def speak(self):
        return "woof!"
    

class Cat(Animal):

    def speak(self):

        return "Meow!"
    


def make_animal_speak(animal):

    print(animal.speak())


dog = Dog()
cat = Cat()


make_animal_speak(dog)
make_animal_speak(cat)


