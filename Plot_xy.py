from matplotlib import pyplot as plt

X = range(-100,100)

## For Y=X
Y = [x*x for x in X]

## For Y=X^2
# Y = [x for x in X]

plt.plot(X,Y)
plt.title('Stats')
plt.xlabel('Value of X')
plt.ylabel('Value of Y')
plt.show()