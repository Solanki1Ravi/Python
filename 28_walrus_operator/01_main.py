# Walrus Operator allows us to assign a value to a variable within an expression. 

# This can be useful when we need to use a value multiple times in a loop, but don’t want to repeat the calculation.

# syntax (:=)


# without walrus operator 
# foods = list()

# while True:
#     food = input("Enter the name of  food you like ")
#     if food =="quit":
#         break
#     foods.append(food)


# print(foods)



# with walrus operator 
foods = list()
while food := input("Enter the name of food you like:- ") !="quit":
    foods.append(food)

print(foods)    