# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 12:00:40 2022

@author: Student
"""
n=int(input("最小范围="))         #取值最小范围
m=int(input("最大范围="))         #取值最大范围
if n<0 or m<=0 or m<n:            #不符合条件时操作
    print("重新输入")
while n<0 or m<=0 or m<n:
    n=int(input("最小范围="))
    m=int(input("最大范围="))
def fx (x):                      #定义质数函数
    for i in range(2,x):
        if x%i==0:
            return False
    return True
h=0
if n<2:
    for i in range(2,m+1):      #最小值小于2时输出方式
        if fx(i)==True:
            print(i)
            h=h+1
    print("个数：",h)
else:
    for i in range(n,m+1):      #最小值大于2时输出方式
        if fx(i)==True:
            print(i)
            h=h+1
    print("个数：",h)
            
        
