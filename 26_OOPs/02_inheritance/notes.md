
# Inheritance
- Inheritance allows us to define a class that inherits all the methods and properties from another class.

- Parent class is the class being inherited from, also called base class.

- Child class is the class that inherits from another class, also called derived class

## Syntax

```python


class Employee:
    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept = dept

    def showInfo(self):
        print(f"Name:- {self.name}\nId:- {self.id}\nDepartment:- {self.dept}")    


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")


e4 = Programmer("Bharat Chhedawal",120,"Sr. Manager")
e4.showInfo()
e4.showLanguage()        


```


# Types of Inheritance 

1. Single Inheritance

2. Multiple Inheritance

3. Multilevel Inheritance

4. Hybrid Inheritance



# Access Modifiers 

# 1. Public 
- Attributes are public by default, meaning they can be accessed from anywhere, both inside and outside the class.

```python

class MyClass:
    def __init__(self):
        self.public_var = "I am public"

obj = MyClass()
print(obj.public_var)  # Accessible everywhere

```

# 2. Private

- Prefix an attribute with double underscores( __ )to make it private. This mangles the attribute's name to make it hard to access from outside the class

```python
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # Correct way to access private attributes
print(obj.__private_var)  # AttributeError: 'MyClass' object has no attribute '__private_var'



```

# Protected

- To indicate a protected attribute, prefix it with a single underscore (_). It's a convention that signals “please don’t touch this unless you’re a subclass.”

```python
class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"

class MySubClass(MyClass):
    def __init__(self):
        pass
obj = MySubClass()
print(obj._protected_var)  # Accessible, but not recommended


```