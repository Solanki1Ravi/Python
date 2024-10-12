

'''
1. The main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.


'''





# class Geeks():
#     def __init__(self):
#         self._age = 0

#     @property
#     def age(self):
#         print("Getter method is called")   
#         return self._age
    
#     @age.setter
#     def set_age(self,a):
#         if(a<18):
#             raise ValueError("Sorry Your age is less than 18")
#         print("Setter method is called ")
#         self._age = a



# m = Geeks()
# # m.set_age = 9
# print(m.set_age)        






class Person():
    def __init__(self,name,age):
        self._name = name
        self._age =age
        

    @property
    def name(self):
        return self._name    
    
    @name.setter
    def set_name(self,value):
        if not value:
            raise ValueError("Name cannot be emapty ")
        self._name = value


    @property
    def age(self):
        return self._age

    @age.setter
    def set_age(self,value):
        if(value<0):
            raise ValueError("Age can't be negative")

        self._age = value


a = Person("Ravi",22)    
print(a.name)
print(a.age)        
g = Person("Ravindra Solanki",12)    
print(g.name)
print(g.age)        
e = Person()
e.name = ""
e.age = 78  
print(e.name)   
print(e.age)   

