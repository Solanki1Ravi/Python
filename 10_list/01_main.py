'''
# Lists are used to store multiple items in a single variable

# List items are ordered, changeable, and allow duplicate values


'''


myList = [10,30.3,True,3,10,"Ravindra Singh",3]
# print(myList)
# print(type(myList))
# print(len(myList))


# Accessing list items 

# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])

# changing list items 

# myList[1]= "Ravi Solanki";
# print(myList)


# checking if item exist or not 

if 10 in myList:
    print("value is present in the list ")

else:
    print("value is not present in the list ")


# Range of Negative Indexes

for i in myList[-8:-1]:
    print(i)
