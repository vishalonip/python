n=int(input())
mat=list(input())
trace=0
def printDiagonalSums(mat, n): 
    for i in range(n):
        for j in range(n): 
            # Condition for secondary diagonal 
            if ((i + j) == (n - 1)): 
                trace*= mat[i][j]
print(trace)