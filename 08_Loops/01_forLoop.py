
'''
==> A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


==> The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

==> With the continue statement we can stop the current iteration of the loop, and continue with the next

==> With the break statement we can stop the loop before it has looped through all the items

'''
# Looping through the string 
Names = "Ravindra Singh";
# for name in Names:
#     print(name)

# range() function 

# for i in range(10):
#     print(i)    


# range with start and end values

# for i in range(5,100):
#     print(i)    

# range with start, end and stop value

# for i in range(5,100,2):
#     print(i)    

# break statement

# for i in range(5,100):
#     # print(i)
#     if(i==55):
#         break


#     print(i)


# continue statement 


  
# for i in range(5,100):
#     # print(i)
#     if(i==55):
#         continue


#     print(i)



# Nested for-loops
myList = ["red","orange","Peach","Green"]

# for color in myList:
#     print(color)
#     for i in color:
#         print(i)
    

# multiplication table of a number using for loop

num = int(input("Enter a number "))
for i in range(1,11):
    print(num,"*",i,"=", (num*i))    
else:
    print("Not in the for loop")    