import math
# exec'('*999999
# setrecursionlimit(999999)
n=int(input())
Sum_of_Sqr=int(n*(n + 1)*(2*n + 1)/6)
#Sum_of_Sqr=(n*(n + 1)*(2*n + 1)/6)
Sum=int((n*(n+1)/2)**2)
# Sum=(n*(n+1)/2)
# Sum_square=(Sum**2)
Diff=Sum-Sum_of_Sqr
print(int(Diff))