# -*- coding: utf-8 -*-
from math import sin

# loti daudz mainigo((
# a0 a1 a2 a3
# s0 s1 s2 s3 ->s (get rid of )

x =float(input("Ievadi skaitli x: "))
#print type(x)

y=sin(x)
print "sin(%6.2f)=%6.2f"%(x,y)

a=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
s=a
print "a0=%6.2f s0=%6.2f"%(a,s)

#a1=(-1)**1*x**3/(1*2*3)
a=a*(-1)**1*x**2/(2*3)
#s1=a0+a1
s=s+a
print "a1=%6.2f s1=%6.2f"%(a,s)

#a2=(-1)**2*x**5/(1*2*3*4*5)
a=a*(-1)**1*x**2/(4*5)
#s2=(a0+a1)+a2
s=s+a
print "a2=%6.2f s2=%6.2f"%(a,s)

#a3=(-1)**3*x**7/(1*2*3*4*5*6*7)
a=a*(-1)**1*x**2/(6*7)
#s3=(a0+a1+a2)+a3
s=s+a
print "a3=%.2f s3=%.2f"%(a,s)
