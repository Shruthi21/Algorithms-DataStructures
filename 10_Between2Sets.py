#!/bin/python

import sys
def GetFactor(n):
    factor = []
    if n> 1:
        factor.append(1)
        factor.append(n)
        for i in range(1,n):
            for j in range(1,n):
                if i * j == n:
                    if i not in factor:
                        factor.append(i)
                    if j not in factor:
                        factor.append(j)
    elif n == 1:
        factor.append(n)
    return factor

def list_compare(list1,list2):
    for l1 in list1:
        if l1 not in list2:
            print l1
            print GetFactor(l1)
            
            return False
    return True

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))


if len(a) == n and len(b) == m:
    a_factor = []
    b_factor = []
    x = []
    for a_element in a:
        a_factor = a_factor + GetFactor(a_element)
    

    for b_element in b:
        b_factor = b_factor + GetFactor(b_element)
        

    print a_factor
    print b_factor
    print max(a)
    print min(b)
    new_factor = []
    
    
    for i in range(max(a),min(b)+1):
        print i
        print GetFactor(i)
        
        
        if i in b_factor:
            new_factor = GetFactor(i)
            new_factor.remove(i)
            print new_factor
            print a_factor
            if list_compare(new_factor,a_factor,):
                if i not in x:
                    x.append(i)
                    print x
                
    print len(x)    
    print x
    
        


        
        
