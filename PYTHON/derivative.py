# -*- coding: utf-8 -*-
#www.cplusplus.com/reference/cstdio/printf
import numpy as np
import matplotlib.pyplot as plt

def mans_sinuss(x):
 k=0 
 a=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
 s=a
 
 while k < 500: 
  k=k+1
  a=a*(-1)*x**2/((2*k)*(2*k+1))
  s=s+a
 return s

a=0
b=3*np.pi
x=np.arange(a,b,0.05)
y=mans_sinuss(x)
plt.plot(x,y)
plt.grid()
#plt.show()

n=len(x)
y_prim = []
for i in range(n-1):
    #print i, x[i], y[i],
    delta_y = y[i+1]-y[i]
    delta_x = x[i+1] -x[i]
    #y_prim = delta_y/delta_x
    #print y_prim
    y_prim.append(delta_y/delta_x)
y_primprim = []    
for j in range(n-2):
    delta_y_prim=y_prim[j+1]-y_prim[j]
    y_primprim.append(delta_y_prim/delta_x)
    

plt.plot(x[:n-1],y_prim)
plt.plot(x[:n-2],y_primprim)
plt.show()
