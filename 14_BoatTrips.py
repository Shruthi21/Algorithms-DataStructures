#!/bin/python

import sys

def BoatTrip(n,c,m,p):
    capacity = c * m
    flag = 0
    if len(p) == n:
        if max(p) > capacity:
            return 'No'
        else:
            return 'Yes'



if __name__ == '__main__':
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    p = map(int, raw_input().strip().split(' '))
    print BoatTrip(n,c,m,p)     
