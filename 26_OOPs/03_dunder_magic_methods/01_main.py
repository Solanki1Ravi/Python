
'''

--> Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading. 
'''

class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id


    def empInfo(self):
        print(f"Name:- {self.name}\nId:-{self.id}")



print(dir(str))

        