
# The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.






# def double(n):
#     return n*2

num = [10,5,12,59,8]

mySumList = list(map(lambda x: x*2,num))
mySumSet = set(map(lambda x: x*2,num))
mySumtuple = tuple(map(lambda x: x*2,num))

print(mySumList)
print(type(mySumList))
print(mySumSet)
print(type(mySumSet))
print(mySumtuple)
print(type(mySumtuple))

