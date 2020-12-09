n=int(input())
a=1
b=1
print(a)
print(b)
for _ in range(2,n):
    next=a**2 + b**2
    print(next)
    a=b
    b=next
