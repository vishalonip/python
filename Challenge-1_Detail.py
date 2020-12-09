n = int(input("Enter the value of n between 0 & 100: "))

if n>=100 or n<0:
    print("The value n should be greater than 0 but less than 100")
    exit

else:
    for x in range(n+1):
        print("#"*x)