a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]    # all number less than 10
for num in range(0,len(a)):
    if int(a[num])<10:
        b.append(a[num])
print(b)
