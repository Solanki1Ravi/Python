'''
1. A constructor is a special method in a class used to create and initalize an object of a class.

2. Constructor invoked automatically when an object of a class is created

3. the main function of a constructors is to initialize of assign values to the data members of that class. 

4. It cannot return any value other than none.


 sytax:

 class name:
    def __init__(self):
        #code

        

# types of constructor in python
1. Parameterized constructor
  --> when the constructor accept the arguments along with the self, it is known as parameterized constructor
  
2. Non-parameterized / default constructor 
   -->  when the constructor doesn't accept any arguments along with the self, it is known as non-parameterized constructor       
'''


class Person:

    def __init__(self):
        print("i'm a non-parameterised constructor")
   # parameterised constructor 
    # def __init__(self,name,age,occupation,email):
    #     self.name = name
    #     self.age = age
    #     self.occupation = occupation
    #     self.email = email


    def info(self):
        print(f"{self.name} is a {self.occupation}, he is {self.age} years old and his email address is {self.email}")




# a = Person("Ravindra Singh",22,"Software Developer","rajnesjse@gamli.com")
# a.info()
d  = Person()



        