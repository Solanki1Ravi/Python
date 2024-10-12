def main():
    N = int(input("Enter the range "))
    # YOUR CODE GOES HERE
    
    for i in range(1,N):
        if i %2 != 0:
            print(i)

    return 0

if __name__ == '__main__':
    main()