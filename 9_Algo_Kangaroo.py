#!/bin/python

import sys


def calculate(x1,v1,x2,v2):
    jump1=1
    jump2=1
    distance1=x1+v1
    distance2=x2+v2
    if (x2>x1 and v2>v1) or (x1>x2 and v1>v2):
        return 'NO'
    
    while distance1!= distance2:
        distance1+= v1
        jump1 = jump1+1
        distance2+= v2
        jump2= jump2+1
        if x2>x1 and v1>v2 and distance1>distance2:
            return 'NO'
        if x1>x2 and v2>v1 and distance2>distance1:
            return 'NO'
        if (x1>x2 or x2>x1 ) and v1==v2:
            return 'NO'
        

         
    if jump1 == jump2:
        return 'YES'
    else:
        return 'NO'


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
print calculate(x1,v1,x2,v2)



    
    
