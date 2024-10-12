class MyClass:
    def __init__(self):
        print("I am protected in mainclass")


    def _funName(self):
        return "It is so much fun here "      

class MySubClass(MyClass):
    def __init__(self):
       print("I am protected in subclass")

     


obj = MySubClass()
print(obj._funName())
