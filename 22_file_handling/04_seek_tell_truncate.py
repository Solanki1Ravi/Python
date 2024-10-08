
'''
# seek():- 

1. The seek() function allows us to move the current position within a file to a specific point.

2. The position is specified in the bytes, and we can move either forward or backward from the current position.


# tell():- 

1. The tell() function returns the current position withtin the file, in bytes. 

2. This can be useful for keeping track of our location within the file or for seeking to a specific position relative to the current position.



# truncate():-

1. When we open a file in python using the open function, we can specify the mode in which we want to open the file.

2. if we specify the mode as "w" or "a", the file is opened in the write mode and we can write to the file. 

3. However, if we want to open the truncate the file to a specified size, we can use the truncate function() 


'''


'''
with open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt","r") as f:
    f.seek(20)

    data = f.read(5)
    print(data)   
'''
 
'''
with open("D:\\GitHub-local\\Python\\22_file_handling\\notes.txt","r") as f:
    # f.seek(20)

    data = f.read(5)
    print(data)  


    curr_pos = f.tell()
    print("Current Position:- " ,curr_pos)


'''
with open("D:\\GitHub-local\\Python\\22_file_handling\\sampel.txt","w") as f:
    f.write("Hello, python world")
    # print(f.truncate(4))
with  open("D:\\GitHub-local\\Python\\22_file_handling\\sampel.txt","r") as d:
    print(d.read())