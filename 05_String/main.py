# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# Strings are immutable means we can't change the string after creating

name = 'Ravi'
# myName = "Ravindra Singh";
# print(name)
# print(myName)


# Multiline Strings:- We can assign a multiline string to a variable by using three(double or single) quote

str1 = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

str2 = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
# print(str1)
# print("String 2 ",str2)


myName = "Ravindra Singh";
# Get the character at a specific position
'''
print(myName[0])
print(myName[1])
print(myName[2])
print(myName[3])
print(myName[4])
print(myName[5])
print(myName[6])
print(myName[7])
print(myName[8])
print(myName[9])
print(myName[10])
print(myName[11])
print(myName[12])
print(myName[13])

'''

# We have other ways (loops) to get the single elements with less number of lines of code

for char in myName:
    print(char)

