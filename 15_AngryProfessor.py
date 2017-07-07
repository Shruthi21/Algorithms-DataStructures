#!/bin/python

import sys

def AngryProfessor(n,k,a):
    counter = 0
    if len(a) == n:
        for e in a:
            if e <= 0:
                counter+=1

        if counter < k:
            return 'YES'
        else:
            return 'NO'



if __name__ == '__main__':
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n,k = raw_input().strip().split(' ')
        n,k = [int(n),int(k)]
        a = map(int,raw_input().strip().split(' '))
        print AngryProfessor(n,k,a)
