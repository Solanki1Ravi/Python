


class Employee:
    def __init__(self,name,age,gender,salary):
        self.name = name
        self.age =age
        self.gender = gender
        self.salary = salary

    def show(self):
        print(f"The name of Employee is {self.name}. He is {self.age} years old. The gender of employee is {self.gender} and the salary is {self.salary}") 


class Address:
    def __init__(self, name, age, gender, salary,address):
        super().__init__(name, age, gender, salary)
        self.address = address

    def show(self):
       super().show()
       print(f'And the address of employee is {self.address}')
                   


# class Emp1(Address,Employee):
#     def __init__(self, name, age, gender, salary, address):
#         super().__init__(name, age, gender, salary, address)

class Emp1(Employee,Address):

    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender, salary)
    
   


ravi = Emp1("Ravindra Singh",22,"M",12000)

ravi.show()

print(Emp1.mro())





'''




class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"The name of Employee is {self.name}") 


class Dancer():
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print(f"The dance style is {self.dance}")


class DancerEmployee(Employee,Dancer):
    def __init__(self, name,dance):
        self.name = name
        self.dance = dance
       
        

c = DancerEmployee("Ravindra Singh","Kathak")
print(c.name)
print(c.dance)  
c.show() 

'''                            