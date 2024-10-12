

class Person:
    name="Ravindra Singh"
    occupation="Software Developer"
    age=22
    email="@raj345@gmail.com"


    def walk(self):
        return f"{self.name} can walk"

    def eat(self):
        return f"{self.name} can eat"    
    
    def info(self):
        print(f"{self.name} is a {self.occupation}. He is {self.age} years old and his gmail address is {self.email}")

ravi = Person()
# print(ravi.name)    
# print(ravi.occupation)    
# print(ravi.age)    
# print(ravi.email)    
# print(ravi.eat())
# print(ravi.walk())
ravi.info()

rahul = Person()
rahul.name = "Rahul Sharma"
rahul.age = 23
rahul.occupation = "Doctor"
rahul.email = "rajil@342@yahoo.com"

# print(rahul.name)
# print(rahul.occupation)
# print(rahul.age)
# print(rahul.email)
# print(rahul.eat())
# print(rahul.walk())
rahul.info()