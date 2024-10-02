

myName = "Ravindra Singh";


# here 0 is included and six is excluded print([0:(n-1)])
print(myName[0:6])

# if we dont't specify the start index then it starts the index from 0 automatically

print(myName[:8])

# if we don't specify the last index then it goes it the last index of string

print(myName[2:])

# if we don't mention either any index(first and last) then it also goess start[0]  to till last index[n-1]
print(myName[:])


# by using len() we can get the length of the entire string

print(len(myName))


# --------Slicing from reverse index------

# print(myName[-1:-5]) # it didn't return anything because it's not the right syntax


# for solve this we write it something like this print(myName(len(myname)-5:len(myName)-1))
print(myName[-5:-1])
