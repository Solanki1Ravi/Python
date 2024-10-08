# In Python, the global keyword is used to modify variables that are outside of the current scope. It enables the programmer to access and change variables that are defined in a global scope from within a function.


x = 90; # global variable

def myFunc():
   global y # now we declared it as the global scope so we can access it in the global scope by default it's scope is local
   y = 9 # local variable
   print(x)

print(x)
myFunc()
print(y) # it gives error because it declared in local scope and we're trying to access it in the global scope