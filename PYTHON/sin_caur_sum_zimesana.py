# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x,n):
 k=0 
 a=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
 s=a

 while k < n: 
  k=k+1
  a=a*(-1)*x**2/((2*k)*(2*k+1))
  s=s+a
 return s

x=np.arange(0.0, 6.28, 0.01) #no 00 lidz 6.28 solis 0.01
y=np.sin(x)
yy=mans_sinuss(x,0)
plt.plot(x,y)
plt.plot(x,yy)
plt.show()
