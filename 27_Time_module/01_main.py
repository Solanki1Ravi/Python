

import time

# s = time.time()
# print(s)



# print(time.gmtime(0))


# currTime = time.ctime(time.time())
# print("Current Time: ",currTime)


# for i in range(50):
#     time.sleep(2)
#     print(i)


# print(time.struct_time())



curTime = time.strftime("%A, %Y-%m-%d, %M:%H:%S",time.gmtime(time.time()))

print(curTime)



# obj1 = time.asctime(time.gmtime(time.time()))
# print(obj1)

# obj2 = time.asctime(time.localtime(time.time()))
# print(obj2)