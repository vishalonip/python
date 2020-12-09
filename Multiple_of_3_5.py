n=int(input())
sum=0
for x in range(1,n):
    if x%3==0 or x%5==0:
        sum+=x
print(sum)