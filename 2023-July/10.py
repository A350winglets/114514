# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:00:21 2022

@author: Student
"""

s=[]
a=int(input("列表项数="))
for i in range(1,a+1):
    s.append(int(input("项目=")))
a=s.__len__()
for i in range (1,a-1):
    if s[i]>s[i+1]:
        s[i],s[i+1]=s[i+1],s[i]
print(s)
