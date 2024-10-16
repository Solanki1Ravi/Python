import shutil as sh
'''
copy()--> this function copies the file located at src to a new location specified by destination. 

--> if the destination location already exist , the original file be overwritten

'''
sh.copy("D:\\GitHub-local\\Python\\29_shutil_method\\01_main.py","D:\\GitHub-local\\Python\\29_shutil_method\\02_copy_main.py")

print("i'm the main file of the shutil module folder and being copied by the copy method in shutil")



# sh.move("D:\\GitHub-local\\Python\\29_shutil_method\\01_copy_main.py", "destination_folder\\")
