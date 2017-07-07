#!/bin/python

import sys


r,c = raw_input().strip().split(' ')
r,c = [int(r),int(c)]
f1 = '..O..'
f2 = 'O.o.O'
f3 = '..O..'
ColumnFlower1 = ''
ColumnFlower2 = ''
ColumnFlower3 = ''
# your code goes here

for i in range(0,c):
    ColumnFlower1 = ColumnFlower1+f1
    ColumnFlower2 = ColumnFlower2+f2
    ColumnFlower3 = ColumnFlower3+f3


for i in range(0,r):
    print ColumnFlower1
    print ColumnFlower2
    print ColumnFlower3
    
        

