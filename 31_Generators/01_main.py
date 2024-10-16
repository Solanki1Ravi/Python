
'''

--> In Python we can create a generator by using the yield statement in the function. The yield returns a value from the generator and suspends the execution of the function until the next value is requested.
'''


def square_list_number(nums):
    for i in nums:
        yield (i*i)


my_num = square_list_number([1,2,3,4,5,6,7,8,9,10]) 

# print(next(my_num))
# print(next(my_num))
# print(next(my_num))
# print(next(my_num))
# print(next(my_num))


for num in my_num:
    print(num)
