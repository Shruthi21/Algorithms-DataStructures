#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
primary = 0    
for i in range(0,n):
    for j in range(0,n):
        if i ==j:
            primary+=a[i][j]
            

secondary=0
start = (n-1)
for i in range(0,n):
    secondary+=a[i][start]
    start-=1

    
res=0

if primary>secondary:
    res = primary-secondary
else:
    res = secondary-primary
    
print res

        


            
    
