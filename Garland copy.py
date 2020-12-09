t=int(input())
if t>101 or t<=0:
    exit(1)

# else:
Garland = list(map(int,input().split(' ')) for x in range(1,t+1))

# Decision for Garland meeting condition
for x in range(1,t+1):
    list1 = sorted(list(Garland[x-1]))
    
    # if int(list1[0]>=1)and (int(list1[2])==int(list1[0]) or int(list1[2])==int(list1[0])+1 or int(list1[0])==int(list1[1]) or (int(list1[1])==int(list1[2]) and (intlist1[0])>=2)):
    # if int(list1[0]>=1)and (int(list1[2])==int(list1[0]) or int(list1[2])==int(list1[0])+1 or int(list1[0])==int(list1[1]) or (int(list1[1])==int(list1[2]) and (intlist1[0])>=2)): 
    # if int(list1[0]>=1) and int(list1[2]>=2) and (int(list1[2])==int(list1[1]) or int(list1[2])==int(list1[0]) or (int(list1[1])==int(list1[0]))):
    if (int(list1[0]>=1)) and ((int(list1[2])-int(list1[1])==int(list1[1])-int(list1[0])) 
    or (int(list1[2])-int(list1[1])==int(list1[1])-int(list1[0]) +1)
    or (int(list1[2])-int(list1[1])==int(list1[1])-int(list1[0]) +2)
    or (int(list1[2])-int(list1[1])==int(list1[1])-int(list1[0])-1 )
    or (int(list1[2])-int(list1[1])==int(list1[1])-int(list1[0])-2 )
    or (int(list1[2])==int(list1[1])+int(list1[0]))
    or (int(list1[2]) == int(list1[0])+ int(list1[1] +1))
    or (int(list1[2]) == int(list1[0])+ int(list1[1] +2))
    or (int(list1[2]) == int(list1[0])+ int(list1[1] -2))
    or (int(list1[2]) == int(list1[0])+ int(list1[1] -1))):
        print("Yes")
    else:
        print("No")