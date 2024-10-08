# To delete a file, you must import the OS module, and run its os.remove() function

import os as o

'''
if o.path.exists("D:\\GitHub-local\\Python\\22_file_handling\\notes.md"):
    d = o.remove("D:\\GitHub-local\\Python\\22_file_handling\\notes.md")

else:
    print("file does not exist")

'''


# Note:-  We can only remove empty folders.
if o.path.exists("D:\\GitHub-local\\Python\\22_file_handling\\data_folder"):
    o.rmdir("D:\\GitHub-local\\Python\\22_file_handling\\data_folder")

else:
    print("File does not exist")    