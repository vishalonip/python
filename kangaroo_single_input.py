a,b,c,d = input().split(' ')

k1=int(a)
v1=int(b)
k2=int(c)
v2=int(d)

result="NO"
for t in range(0,10000):
    if int(k1+v1*t)==int(k2+v2*t):
        # print(t)
        result="YES"
        break
print(result)