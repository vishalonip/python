#write a program to find those numnbers which 
# are divisible by 7 & 5, 
# between 1500 and 2700 (both included)

for num in range (1500, 2701):
    if num%5==0 and num%7==0:
        print(num)

