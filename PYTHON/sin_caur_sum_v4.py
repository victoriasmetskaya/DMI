# -*- coding: utf-8 -*-
from math import sin



x =float(input("Ievadi skaitli x: "))


y=sin(x)
print "sin(%6.2f)=%6.2f"%(x,y)

k=0 
a=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
s=a
print "a%d=%6.2f s%d=%6.2f"%(k,a,k,s)

k=1
a=a*(-1)**1*x**2/((2*k)*(2*k+1))
s=s+a
print "a%d=%6.2f s%d=%6.2f"%(k,a,k,s)

k=2
a=a*(-1)**1*x**2/((2*k)*(2*k+1))
s=s+a
print "a%d=%6.2f s%d=%6.2f"%(k,a,k,s)

k=3
a=a*(-1)**1*x**2/((2*k)*(2*k+1))
s=s+a
print "a%d=%.2f s%d=%.2f"%(k,a,k,s)
