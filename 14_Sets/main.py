
# Sets are used to store multiple items in a single variable.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# Set items are unordered, unchangeable, and do not allow duplicate values.

# Note: Set items are unchangeable, but we can remove items and add new items.

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.




# ravi = {} # this returns dictionary istead of set
#ravi = set() # this returns set when we check  the datatype of this
# print(type(ravi))


thisset = {"apple","Ravi", "banana", "cherry", "cherry","apple"}
# print(thisset)
print(len(thisset))
# Accessing set items 
for value in thisset:
    print(value)