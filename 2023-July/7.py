# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:14:02 2022

@author: Student
"""

def f(a,b,c,d):
    e=(((a-c)**2)+((b-d)**2))**(1/2)
    return e

x1=float(input("x1="))
y1=float(input("y1="))
x2=float(input("x2="))
y2=float(input("y2="))
x3=float(input("x3="))
y3=float(input("y3="))
c=f(x1,y1,x2,y2)
c=c+f(x1,y1,x3,y3)
c=c+f(x2,y2,x3,y3)
print(c)
