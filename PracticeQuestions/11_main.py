#Return the factorial of the number N
def factorial(N):

                
    # Your code goes here
    
    fact = 1;
    if N==0 or N==1 :
        return 1
    else:    
        for i in range(1,N + 1):
            fact = fact*i


        print(f"The factorial of",N,"is",fact )

        
    return fact  
    

factorial(5)