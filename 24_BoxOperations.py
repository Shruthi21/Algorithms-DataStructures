#!/bin/python

import sys

def PerformOperation(n,operation,box):
    if len(box) == n:
        if len(operation) == 3 or len(operation) == 4:
            if operation[0] == 1:
                for i in range(operation[1], operation[2]+1,+1):
                    box[i] = box[i]+operation[3]
            elif operation[0] == 2:
                for i in range(operation[1],operation[2]+1,+1):                    
                    box[i] = box[i]/operation[3]

                    
            elif operation[0] == 3:                               
                print min(box[operation[1]:operation[2]+1])
            
                          
            elif operation[0] == 4:
                               
                result = 0
   
                for i in range(operation[1],operation[2]+1,+1):
                    result+= box[i]
                print result          
                
                          
                          
if __name__ == '__main__':
    n,q = raw_input().strip().split(' ')
    n,q = [int(n),int(q)]
    box = map(int, raw_input().strip().split(' '))
    # your code goes here
    while q!=0:
        q-=1
        operation = map(int, raw_input().strip().split(' '))
        PerformOperation(n,operation,box)

        
    
