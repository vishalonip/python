import random

list_1=[]

for randomNumber in range(1,100):
    randNum=random.randint(1,10000)
    list_1.append(randNum)
print(list_1)

max_num = int(list_1[0])
for element in list_1:
    if element > max_num:
        max_num = element
print("max_num of list_1 is", max_num)