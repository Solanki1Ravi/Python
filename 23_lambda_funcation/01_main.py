'''
# lambda function():- 

1. In python, lambda function is a small anonymous function without a name.

2. lambda function are often used in situation where a small function is required for a small period of time. 

3. They are commonly used as arguments to higher order function, such as map, filter, and reduce.


syntax:

lambda arguments: expression

'''

cube = lambda x : x*x*x
Mysum = lambda a,b,c:a+b+c
MyAvg = lambda a,b,c:(a+b+c)/3

# print(cube(5))
# print(Mysum(10,20,30))
# print(MyAvg(10,20,30))

# passing function as arguments 

def appl(cube,value):
    return 6+cube(value)


print(appl(cube,5))