n = int(input())
if n>=100 or n<0:
    exit
else:
    for x in range(1,n+1):
        print("#"*x)