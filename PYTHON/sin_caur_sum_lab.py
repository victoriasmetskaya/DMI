# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
 k=0 
 a=(-1)**0*x**1/(1) #ja int tad rez = int -vesels skaitlis
 s=a
 print "Summas pirmais saskaitamais: a%d=%6.2f s%d=%6.2f"%(k,a,k,s)

 while k < 500: 
  k=k+1
  a=a*(-1)*x**2/((2*k)*(2*k+1))
  s=s+a
  if k==499: 
   print "a499=%.2f"%(s) 
 print "a500=%.2f"%(s)
 return s

x=float(input("Ievadi skaitli x: "))
y=sin(x)
print "funkcijas skaitlis: sin(%6.2f)=%6.2f"%(x,y)
yy = mans_sinuss(x)
print "summas skaitlis: sin(%.2f)=%.2f"%(x,yy)
print "    500"
print "   ----"
print "    \  (-1)^k * x^(2k+1) "
print "S =  > ------------------"
print "    /  (2k+1)! "
print "   ----"
print "    k=0"
print " "
print "    (-1) * x^2"
print "R = -----------" 
print "    2(2k+1)(2k)"
