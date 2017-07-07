#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
c = map(int, raw_input().strip().split(' '))
# your code goes here
candy = 0
b = n
for i in range(0,(len(c)-1)):
    if (b - c[i]) < 5:

        candy+= (n - (b - c[i]))

        b = n

    else:
        b = b - c[i]


print candy
