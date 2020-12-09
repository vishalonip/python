n=int(input())
Multi=int(7**n)
sum_of_Digits=0
for digit in str(Multi):
    sum_of_Digits+=int(digit)
print(sum_of_Digits)