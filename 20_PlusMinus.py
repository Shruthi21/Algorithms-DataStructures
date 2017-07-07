#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positive =0.000000
negative = 0.000000
zero=0.000000
for a in arr:
    if a>0:
        positive+=1
    elif a<0:
        negative+=1
    else:
        zero+=1
        
print format(positive/n,'.6f')
print format(negative/n,'.6f')
print format(zero/n,'.6f')
        
       
        
