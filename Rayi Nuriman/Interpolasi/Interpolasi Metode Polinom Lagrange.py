import numpy as np #panggil library

x = np.array([0, 0.4, 0.8, 1.2],float)
y = np.array([1, 0.921061, 0.696707, 0.362358],float)
n = len(x)
d = n-1

xp = float(input("X = "))
yp = 0

for xi,yi in zip(x,y):
  yp += yi*(np.prod((xp - x[x != xi])/(xi-x[x != xi])))

print("x = %.2f, y = %.3f" % (xp,yp))