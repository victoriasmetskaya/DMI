# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
 k=0 
 a=(-1)**0*x**1/(2) #ja int tad rez = int -vesels skaitlis
 s=a
 print "(izdruka no liet. funkc)a%d=%6.2f s%d=%6.2f"%(k,a,k,s)

 while k < 500: 
  k=k+1
  a=a*(-1)*x**2/(4*(2*k)*(2*k+1))
  s=s+a
  if k==499: 
   print "a499=%.2f"%(s) 
 print "a500=%.2f"%(s)
 return s
 
x=float(input("Ievadi skaitli x: "))
y=sin(x*0.5)
print "funkcijas skaitlis: sin(%6.2f/2)=%6.2f"%(x,y)
yy = mans_sinuss(x)
print "summas skaitlis: sin(%.2f/2)=%.2f"%(x,yy)

