

'''

# return statement:- The return statement is used to return the value of the expression back to the calling function

1. Keyword Arguments:- We can also send arguments with the key = value syntax. This way the order of the arguments does not matter


# variable length arguments: 
--> If we do not know how many arguments that will be passed into our function, add a * before the parameter name in the function definition.

--> This way the function will receive a tuple of arguments, and can access the items accordingly


'''



# function with default arguments

# def userInfo(name,age,country="india"):
#     print("Name: ",name,"\n","Age: ",age,"\n","Conntry: ",country)


# name = input("Enter Your Name: ")
# age = int(input("Enter Your Age: "))
# Country = input("Enter Your country: ")
# userInfo(name,age)


# function with keyword arguments
def userInfo(name,age,country="india"):
    print("Name: ",name,"\n","Age: ",age,"\n","Conntry: ",country)

# userInfo(age=22,country="norway",name="Amy jones")  



# variable length arguments

# def my_function(*kids):
#   print(type(kids))
#   print("The youngest child is " + kids[2])
#   print("The Oldest child is " + kids[0])
#   print("The Middle child is " + kids[1])

# my_function("Emil", "Tobias", "Linus")


# Required arguments

def my_function(fchild,schild,tchild):
  print("The youngest child is " + fchild)
  print("The Oldest child is " + schild)
  print("The Middle child is " + tchild)

#my_function("Emil", "Tobias") # returns error

my_function("Emil", "Tobias","Ravindra Solanki")