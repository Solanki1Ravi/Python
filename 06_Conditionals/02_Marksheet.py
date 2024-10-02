marks = float(input("Enter Your Marks: "))

if(marks<=100 and marks>=91):
    print("Grade A")

elif(marks<=90 and marks>=81):
    print("Grade B")

elif(marks<=80 and marks>=71):
    print("Grade C") 
elif(marks<=70 and marks>=61):
    print("Grade D")       
elif(marks<=60 and marks>=51):
    print("Grade E")       
else:
    print("Grade F")    