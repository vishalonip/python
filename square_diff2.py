def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)

n=int(input())
Sum_of_Sqr=int(sum_n(n)*(2*n + 1)/3)
Sum=int(sum_n(n)*sum_n(n))
Diff=Sum-Sum_of_Sqr
print(Diff)
# else:
#     exit