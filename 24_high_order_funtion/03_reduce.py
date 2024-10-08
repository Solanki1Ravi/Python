
'''
--> The reduce function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

--> This function is defined in “functools” module.
'''


from functools import reduce


myLis = [10,22,65,84,51,84,8,41,20]

myNewLis = reduce(lambda x,y:x+y,myLis)
print(myNewLis)