
# A function is a block of code which only runs when it is called.

# A function can return data as a result.\

# We can pass data, known as parameters, into a function.

# function definitions cannot be empty, but if for some reason we have a function definition with no content, put in the pass statement to avoid getting an error

'''
syntax:

def function_name(parameters(if required)):
    body of function

'''

# function without arguments 

def greet():
    print("Hello Everyone, Good morning")

greet()    


# function with arguments 
def Greet(name):
    print("Hello,",name)


# name = input("Enter a name: ")
# Greet(name)    


# pass statement

def myFunc():
    pass

