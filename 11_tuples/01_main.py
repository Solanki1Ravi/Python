'''
# Tuples are written with round brackets.Tuples are used to store multiple items in a single variable

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Tuple items are ordered, unchangeable, and allow duplicate values.

# To create a tuple with only one item, you have to add a comma after the item


'''


mytup = (10,20,33,45,78,95);
# print(mytup)
# print(type(mytup))

#mytup1 = (1) # it is int now for change it in tuple we have to add comma in the end of first value 

mytup1 = (1,)
# print(mytup1)
# print(type(mytup1))

# accessing tuple items 
# print(mytup[0])
# print(mytup[1])
# print(mytup[2])
# print(mytup[3])
# print(mytup[4])

# trying to change the tuple items 
# mytup[4]= 456468 # returns error because we can't change the tuple items 
# print(mytup)

# if we want to change the tuple items then first we change the tuple into list and after changing the items convert it into tuple again 
'''


# converting the tuple into list 
mytupList = list(mytup)
mytupList.append("Ravindra Singh")
print(type(mytupList))
print(mytupList)

# converting the list into tuple
mytup = tuple(mytupList)
print(type(mytup))
print(mytup)
'''


# looping on a tuple
for i in mytup:
    print(i)