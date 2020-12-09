import random

list_1 = []

for randomNumber in range(1,6):
    randNum=random.randint(1,10000)
    list_1.append(randNum)

print (list_1)
print (sorted(list_1))
print (sorted(list_1)[-1])