
'''

1. In Python, the super() function is used to refer to the parent class or superclass. 

2. It allows us to call methods defined in the superclass from the subclass, enabling us to extend and customize the functionality inherited from the parent class

'''


class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id

    def show(self):
        print(f"The Name of employee is {self.name} and the id of employee is {self.id}.")    

class Role(Employee):
    def __init__(self, name, id,role):
        super().__init__(name, id)
        self.role = role


    def childClass(self):
        super().show()
        print(f"the role of the employee is {self.role}")
        
class Address(Role):
    def __init__(self, name, id, role,address):
        super().__init__(name, id, role)
        self.address = address


    def empAddress(self):
        super().childClass()
        print(f"The Address is {self.address}")    


# emp1 = Employee("Ravindra Singh",122)
# emp1.show() 


# emp2 = Role("Ravindra Singh",123,"Python Developer")
# print(f"Name:- {emp2.name}\nId:- {emp2.id}\nRole:-{emp2.role} ")
# emp2.childClass()


emp2 = Address("Ravindra Singh",123,"Python Developer","sikar")
print(f"Name:- {emp2.name}\nId:- {emp2.id}\nRole:-{emp2.role}\nAddress:- {emp2.address} ")
emp2.empAddress()



