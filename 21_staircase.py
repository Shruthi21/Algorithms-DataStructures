#!/bin/python

import sys


n = int(raw_input().strip())
stair = ''
for i in range(0,n):
    stair = stair + ' '
stair_list= list(stair)
for i in range(n-1,-1,-1):
    stair_list[i] = '#'
    print "".join(stair_list)
    
