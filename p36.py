# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:21:36 2022

@author: Student
"""

rate=[0.0325,0.03,0.03,0.02,0.0175]
benjin=50000
yrs=5
tot=0
for i in range(1,yrs+1):
    benjin=benjin*(1+rate[(i-1)])
    print(benjin)
    