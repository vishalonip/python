t1=input()
try:
    t = int(t1)
    if t>10000 or t<1:
        # print("NO")
        exit(1)
    else:
        ni = []
        for x in range(1,t+1):
            ni.append(input())

        for x in range(1, t+1):
            try:
                int1 = int(ni[x-1])
                if int1 >=3 and int1%4==0 and int1 <=1000000000:
                    print("YES")
                else:
                    print("NO")
            except :
                print("NO")
except :
    exit(1)                
