


n = 5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")


    print()

for s in range(n-1):
    for a in range(s):
        print(" ",end=" ")

    for o in range(s,n-1):
        print("*",end=" ")

    for q in range(s,n):
        print("*",end=' ')     



    print()    


