# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:40:15 2022

@author: Student
"""

s=[1919810,12312,112,12412,114514,1,25]
a=s.__len__()
for i in range (1,a-1):
    if s[i]>s[i+1]:
        s[i],s[i+1]=s[i+1],s[i]
print(s)
