t=int(input())
try:
    ni = []
    for x in range(1,t+1):
        ni.append(input())

    for x in range(1,t+1):
        try:
            int1 = int(ni[x-1])
            if int1 >=3 and int1%4==0:
                print("YES")
            else:
                print("NO")
        except :
            print("NO")
except  :                
    exit()