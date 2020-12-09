from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

X1 = range(-100,100)
Y1 = [x for x in X1]

X2 = range(-100,100)
Y2 = [x*x for x in X2]

plt.plot(X1,Y1,'g',label='Y=X',linewidth=3)
plt.plot(X2,Y2,'b',label='Y=X^2',linewidth=6)
plt.legend()
plt.title('Stats')
plt.xlabel('Value of X')
plt.ylabel('Value of Y')
plt.show()