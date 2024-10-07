

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.



try:
    # a = int(input("Enter a number: "))
    # print(f"Multiplication table of {a} is: ")
    # for i in range(1,11):
    #     print(f"{a} x {i} = {a*i}")
    

    a = [89,9898,90]
    print(a[40])

except IndexError:
    print("index out of bound exception")     
except Exception as e:
    print(e) 
# else:
#     print("Nothing went wrong")    
      
finally:
    print("I'll execute in every condition") 




# -----------raising custom error 


# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.


    num = int(input("Enter a number: "))
    if num <0:
        raise Exception("Value can't be less than 0")
    else:
        print(num)
