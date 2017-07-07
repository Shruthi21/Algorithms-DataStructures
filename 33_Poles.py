#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = []
w = []
for a0 in xrange(n):
    x_i,w_i = raw_input().strip().split(' ')
    x_i,w_i = [int(x_i),int(w_i)]
    x.append(x_i)
    w.append(w_i)
cost = 0
if k == 1:
    for i in range(len(x),0,-1):
        if i > 0:
            cost+=(w[i] * (x[i-1] - x[i]))
elif k > 1:
    MaxWeight = max(w)
    for i in range(0,len(x)):
        if w[i] == MaxWeight:
            
            
            
    
    
    
    
            
        
        
    
