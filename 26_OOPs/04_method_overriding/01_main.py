'''
--> Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.

'''
class Animal:
    def __init__(self):

        print("Animal have some properties")
      
    def move(self):
        print("Animal move in all directions")

    def eat(self):
        print("Animal eats food")

class Dog(Animal):

    def __init__(self):
        super().__init__()

    def move(self):
        print("Dog can move in all directions")

    def eat(self):
        print("dog eats dog food")  



dog = Dog()
dog.eat()                 
dog.move()                   