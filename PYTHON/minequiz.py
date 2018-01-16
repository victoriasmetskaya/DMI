import random
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
 k=0 
 a=(-1)**0*x**1/(2) #ja int tad rez = int -vesels skaitlis
 s=a
 

 while k < 500: 
  k=k+1
  a=a*(-1)*x**2/(4*(2*k)*(2*k+1))
  s=s+a
 return s

N = 100000
x = []
y = []
a = 0
b = np.pi
c = -1
d = 1

for i in range(N):
    x.append(random.uniform(a,b))
for i in range(N):
    y.append(random.uniform(c,d))

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_sinuss(x[i]) and y[i] > 0) \
    or (y[i] > mans_sinuss(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()
plt.show()

areaRect = (b-a)*(d-c)
areaSin = areaRect * len(green_x) / N
print areaSin
