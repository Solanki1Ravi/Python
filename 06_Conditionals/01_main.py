'''

Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b


==> And:- The and keyword is a logical operator, and is used to combine conditional statements. In the And both the conditional must be true then it returns true else if returs false

==> Or:- The or keyword is a logical operator, and is used to combine conditional statement. In the or if the conditional become true then it returns true.

==> Not:- The not keyword is a logical operator, and is used to reverse the result of the conditional statement

'''

a = int(input("Enter a number "))
# if-else
'''
if(a>10):
    print("Number is greater than 10")

else:
    print("Number is less than 10")    
'''

# if-elif-else ladder

if(a==0):
    print("Number is Zero")

elif(a>0):
    print("Number is Positive")  

else:
    print("Number is Negative")      