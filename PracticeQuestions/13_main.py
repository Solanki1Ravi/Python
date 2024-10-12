# Swap two numbers 
# 1--> without the help of third variable

'''
a = 1
b = 2
print(f"Before:- a:- {a},b:- {b}")
a = a+b
b = a-b
a = a-b
print(f"After:- a:- {a},b:- {b}")
'''


# 2--> with the help of third variable(using + and -)
# a = 1
# b = 2
# print(f"Before:- a:- {a},b:- {b}")
# c = a
# a = b
# b = c
# print(f"After:- a:- {a},b:- {b}")



# 2--> with the help of third variable(using + and -)

a = 10
b = 20
print(f"Before:- a:- {a},b:- {b}")

b = a*b
a = b//a
b = b//a
print(f"After:- a:- {a},b:- {b}")