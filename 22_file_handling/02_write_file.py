'''
# Write to an Existing File
--> To write to an existing file, you must add a parameter to the open() function:

1. "a" - Append - will append to the end of the file

2. "w" - Write - will overwrite any existing content

'''

# f = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt",'a')

# # f.write("My name is Ravindra Singh")

# d  = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt",'r')
# print(d.read())
# f.close()


#  the "w" method will overwrite the entire file

'''
f = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt",'w')

f.write("My Name is Ravindra Singh")
f.close()

d = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt",'r')
print(d.read())
d.close()


'''

# if the mentioned file doesn't exist in 'w' and 'a' then it create one 
'''


d = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.md",'a')
# print(d)
d.write("# our first comment")
d.close()

f = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.md",'r')
print(f.read())
'''


# Create a New file

# "x" - Create - will create a file, returns an error if the file exist

# myX = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.md",'x') # returns error because it exist
myX = open("D:\\GitHub-local\\Python\\22_file_handling\\notese.md",'x')

print(myX)

myX.close()