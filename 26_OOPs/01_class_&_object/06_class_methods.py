
'''
--> A class method is a type of method that is bound to the class and not the instance of the class.

--> In other words, it operates on the class as a whole, rather than on a specific instance of the class.

--> Class method are defined using the @classmethod decorator, followed by a function definition. 

--> the first argument of the function is always 'cls' , which represent the class itself.



'''



class Employee:
    company = "Apple India"

    def show(self):
        print(f"The name of employee is {self.name} and the company is {self.company}")

    @classmethod
    def changeClass(cls,newCompany):
        cls.company = newCompany    


emp1 =  Employee()
emp1.name = "Ravindra singh"
emp1.show()
emp1.changeClass("Tesla")
emp1.show()
print(Employee.company)
# emp1.changeClass()
