#!/bin/python

import sys

def GreatXOR(x):
    result = []
    for e in x:
        
        i = 1
        counter = 0
        while i < e:
          
            if (i ^ e) > e:
                counter+=1
            i+=1
        result.append(counter)
    return result


if __name__ == '__main__':
    testcase = int(raw_input())
    x=[]
    
    while testcase != 0:
        number = int(raw_input())        
        x.append(number)
        testcase = testcase - 1
    
    for x0 in GreatXOR(x):
        print x0
