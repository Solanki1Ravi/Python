


class Vector():

    def __init__(self,i,j,k):
        self.i = i
        self.j=j
        self.k=k


    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    

    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
    def __sub__(self,x):
        return Vector(self.i-x.i,self.j-x.j,self.k-x.k)
    

    def __mul__(self,x):
        return Vector(self.i*x.i,self.j*x.j,self.k*x.k)




ve1 = Vector(1,2,3)
print("Vector 1:- ",ve1)    


ve2 = Vector(3,8,9)
print("Vector 2:- ",ve2)   

add = ve1+ve2
sub = ve1-ve2
mul = ve1*ve2

print("Addition ",add)
print("Subtraction ",sub)
print("Multiplication ",mul)
# print("Addition ",add)