#!/usr/bin/python
# -*- coding: utf-8 -*-
# garumzimes utt

a=input("ievadi skaitli ")
print (a)," \t%1 \t%2 \t%3 \t%4 \t%5 \t%10"
k=0
while (k < 9):
 u=a % 1
 b=a % 2
 c=a % 3
 d=a % 4
 e=a % 5
 f=a % 10
 print (a), "\t", (u), "\t", (b), "\t", (c), "\t", (d), "\t", (e), "\t", (f)
 k=k + 1
 a=a + 1
#break



'''
#https://www.tutorialspoint.com/unix_commands/echo.htm
print "I am the mountain \vI am the sea \vYou can't take that"
print "\t\t\tThat away from me"
print "\tI am the mountain \nI am the sea"
'''

'''
#example 7
#echo -e 'Here the \rcontent before this is removed.'  
print "Here the \rcontent before this is removed."  
'''

'''
#example 6
#echo -e 'Here \vthe \vspaces \vhave \vvertical \vtab \vspaces.'
print "Here \vthe \vspaces \vhave \vvertical \vtab \vspaces."
'''

'''
#example 5
#echo -e 'Here \tthe \tspaces \thave \thorizontal \ttab \tspaces.'
print "Here \tthe \tspaces \thave \thorizontal \ttab \tspaces."
'''

'''
#example 4
#echo -e 'Here \nthe \nspaces \nare \nnewlined.'
print "Here \nthe \nspaces \nare \nnewlined."
'''

'''
#example 3
# echo -e 'Here \bthe \bspaces \bare \bbackspaced.'
print "Here \bthe \bspaces \bare \bbackspaced."
'''

'''
#1. piemers
print "Hello world!"
'''
