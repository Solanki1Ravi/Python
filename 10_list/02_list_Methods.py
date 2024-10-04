myList = [10,30.3,True,3,10,"Ravindra Singh",3]

# append():- Adds an element at the end of the list
myList.append(465897);

# clear():- Removes all the elements from the list
myList.clear()

# copy():- Returns a copy of the list

myList2 = myList
print(myList2)

# count():- Returns the number of elements with the specified value
print(myList.count(3))

# extend():- Add the elements of a list (or any iterable), to the end of the current list
myList2 = [20,336.9,78,True, False]
myList.extend(myList2)


# index():-  Returns the index of the first element with the specified value


print(myList.index(True))

# insert():- Adds an element at the specified position
myList.insert(3,"Ravi Solanki")
print(myList)

# pop():- Removes the element at the specified position
print(myList.pop(2))
print(myList)

# remove():- Removes the item with the specified value
myList.remove(10)
print(myList)

# sort():- 	Sorts the list by default it ascending order but we can chnage it 
myList1 = [10,87,3.33,98,44,65,20.32]
myList1.sort()
print("Ascending ",myList1)

# reveerse():- Reverses the order of the list
myList1 = [10,87,3.33,98,44,65,20.32]
myList1.sort(reverse=True)
print("Descending ",myList1)