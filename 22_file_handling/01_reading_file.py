# File handling is an important part of any web application.

# Python has several functions for creating, reading, updating, and deleting files.


# File Handling:- 

        # The key function for working with files in Python is the open() function.

        # The open() function takes two parameters; filename, and mode

       # "r" - Read - Default value. Opens a file for reading, error if the file does not exist

        # "a" - Append - Opens a file for appending, creates the file if it does not exist

        # "w" - Write - Opens a file for writing, creates the file if it does not exist

        # "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# We should always close our files, in some cases, due to buffering, changes made to a file may not show until we close the file.


# READING A FILE

f = open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt",'r')

# print(f.read())


# By default the read() method returns the whole text, but We can also specify how many characters We want to return

# print(f.read(10))


# We can return one line by using the readline() method

# print(type(f.readline()))

# We can return whole text in the form of list using readlines() method 
# print(type(f.readlines()))

# looping through the file

for i in f:
    print(i)
f.close()
