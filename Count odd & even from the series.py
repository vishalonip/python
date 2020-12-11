list = (1,2,3,4,5,6,7,8,9)

odd = 0
even = 0

for value in list:
    if value%2 == 0:
        even+=1
    else:
        odd+=1

print ("Odd is" ,odd, "and Even is" ,even,)