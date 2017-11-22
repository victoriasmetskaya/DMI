# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
 k=0 
 a=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
 s=a
 print "(izdruka no liet. funkc)a%d=%6.2f s%d=%6.2f"%(k,a,k,s)

 while k < 3: 
  k=k+1
  a=a*(-1)*x**2/((2*k)*(2*k+1))
  s=s+a
  print "(izdruka no liet f)a%d=%6.2f s%d=%6.2f"%(k,a,k,s)
 print "(izdruka no liet f) done"
 return s

x=float(input("Ievadi skaitli x: "))
y=sin(x)
print "standarta sin(%6.2f)=%6.2f"%(x,y)
yy = mans_sinuss(x)
print "mans sin(%.2f)=%.2f"%(x,yy)

