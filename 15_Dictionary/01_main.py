# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# duplicate keys not allowed values can be duplicate

myInfo = {
    'name':"Ravindra Singh",
    'age':23,
    'married':False,
    'income':0.0,
    'age':56 # it is duplicated but can't print override the current value
}

print(myInfo)

#--------Accessing the dict items ---------- 


# print(myInfo['name'])
# print(myInfo['age'])
# print(myInfo['married'])
# print(myInfo['income'])

# print(myInfo.get('name'))
# print(myInfo.get('age'))
# print(myInfo.get('married'))
# print(myInfo.get('income'))
# print(len(myInfo))

# print(myInfo.keys())  # returns all the keys of dictionary
# print(myInfo.values()) # returns all the values of dictionary
# print(myInfo.items()) # The items() method will return each item in a dictionary, as tuples in a list.

# for x in myInfo:
#     print(f"The value of the key \"{x}\" and the corresponding values is \"{myInfo[x]}\"")


# for key ,value in myInfo.items():
#     print(f"\"{key}\" and the value \"{value}\"")    


# --------changing the dict items---------
# We can change the value of a specific item by referring to its key name:


myInfo['age']=23;
print(myInfo)


# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# myInfo.update({'age':55})
# myInfo.update({'income':5500000})
# myInfo.update({'DOB':'26/06/2002'}) # add the new entry in the dictionary
# print(myInfo)


# Add item in the dict 

myInfo['DOB']=2002
# print(myInfo)


# Remove items 

# pop():- The pop() method removes the item with the specified key name:

# myInfo.pop('age')
# print(myInfo)

# popitem():- The popitem() method removes the last inserted item:

# myInfo.popitem()
# print(myInfo)

#The del keyword removes the item with the specified key name:
# del myInfo['income']
# print(myInfo)

# The del keyword can also delete the dictionary completely:
# del myInfo
# print(myInfo)

# clear():- The clear() method empties the dictionary and returns a empty dictionary:

myInfo.clear()
print(myInfo)