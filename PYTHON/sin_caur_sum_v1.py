# -*- coding: utf-8 -*-
from math import sin

# (1.)*(2)=(2.) - float * int = float
# float(input())
x =float(input("Ievadi skaitli x: "))
#print type(x)

y=sin(x)
print "sin(%.2f)=%.2f"%(x,y)

a0=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
s0=a0
print "a0=%.2f s0=%.2f"%(a0,s0)

a1=(-1)**1*x**3/(1*2*3)
s1=a0+a1
print "a1=%.2f s1=%.2f"%(a1,s1)

a2=(-1)**2*x**5/(1*2*3*4*5)
s2=a0+a1+a2
print "a2=%.2f s2=%.2f"%(a2,s2)

a3=(-1)**3*x**7/(1*2*3*4*5*6*7)
s3=a0+a1+a2+a3
print "a3=%.2f s3=%.2f"%(a3,s3)
