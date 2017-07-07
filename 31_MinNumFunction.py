#!/bin/python

import sys


n = int(raw_input().strip())

start_fun = 'min(int, int)'
concatenate_fun = 'min(int, '
result = ''
if n==2:
    print start_fun
elif n>2:
    result = start_fun
    while n != 2:
        n-=1
        result = concatenate_fun + result + ')'
    print result    
