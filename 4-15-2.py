# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:20:55 2018

@author: Administrator
"""

def  rightShift(arr,k):
    if  arr == None:
        print  "参数不合法"
        return
    lens = len(arr)
    k %= lens
    while  k!= 0:
        t = arr[lens - 1];
        i=lens-1
        while  i>0:
            arr[i] = arr[i - 1]
            i -=1
        arr[0] = t
        k -=1

if  __name__=="__main__":
    k = 4;
    arr= [1, 2, 3, 4, 5, 6, 7, 8]
    rightShift(arr, k)
    i=0
    while  i<len(arr):
        print  arr[i],
        i +=1
