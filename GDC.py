import math

A,B = input().split(' ')

a=int(A)
b=int(B)
fact=1

if a>=b:
    print(math.factorial(b))
else:
    print(math.factorial(a))