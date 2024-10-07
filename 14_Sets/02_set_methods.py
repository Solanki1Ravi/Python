mySet = {10,20,54,"Ravindra Singh",True,22.44}


# add():- Adds an element to the set
# mySet.add(4568)

# clear():- Removes all the elements from the set
# mySet.clear()

# difference():- Returns a set containing the difference between two or more sets
# mySet1 = {55,44,10,20}

# print(mySet.difference(mySet1))

# difference_update():-  The difference_update() method removes the items that exist in both sets

# The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
# mySet.difference_update(mySet1)

# print(mySet)

# print(mySet)

# discard():- The discard() method removes the specified item from the set.

# mySet1.discard(10)
# print(mySet1)

# The intersection() method returns a set that contains the similarity between two or more sets.

# print(mySet.intersection(mySet1))

# Removes the items in this set that are not present in other, specified set(s)
# print(mySet.intersection_update(mySet1))

# isdisjoint():- Return True if no items in set x is present in set y:
# mySet1 = {55,44,108,2.0}
# x = mySet.isdisjoint(mySet1)
# print(x)


# issubset():- Returns whether another set contains this set or not
# mySet1 = {10,20} # true
# mySet1 = {10,20,54,48} # false
# x = mySet1.issubset(mySet)
# print(x)

# issuperset():- Returns whether this set contains another set or not
# mySet1 = {10,20}
# x = mySet.issuperset(mySet1)
# print(x)

# pop():- Removes an element from the set
# mySet.pop()
# print(mySet)

# remove():- Removes the specified element
# mySet.remove(20)
# print(mySet)

# symmetric():- Return a set that contains all items from both sets, except items that are present in both sets

# The returned set contains a mix of items that are not present in both sets.

# mySet1 = {55,44,10,20}
# print(mySet.symmetric_difference(mySet1))


# symmetric_difference_update():- Remove the items that are present in both sets, AND insert the items that is not present in both sets:

# mySet1 = {55,44,10,20}
# mySet.symmetric_difference_update(mySet1)
# print(mySet)

# union():- Return a set that contains all items from both sets, duplicates are excluded:
# mySet1 = {55,44,10,20}
# mySet.union(mySet1)
# print(mySet)

# update():- Insert the items from set y into set x:
mySet1 = {55,44,10,20}
mySet.update(mySet1)
print(mySet)

