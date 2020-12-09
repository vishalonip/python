n = int(input())
if n>=1000 or n<0:
    exit
else:
    for i in range(1,n+1,1):
        number = 0                 # Intitializing the value
        for j in range(1,i+1,1):
            number = (j * 2) -1 
            if(number==1):
                print("[",end="")
            print(number,end="")
            if(j!=i):
                print(", ",end="")            
        print("]")   