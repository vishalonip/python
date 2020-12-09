k1=int(input())
v1=int(input())
k2=int(input())
v2=int(input())
result="No"
for t in range(0,10000):
    if k1+v1*t==k2+v2*t:
        # print(t)
        result="Yes"
        break
print(result)