#!/bin/python

import sys

def CheckWeighted(x,s):
    WeightedString = []
    
    alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
             'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
             'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22,
             'w':23, 'x':24, 'y':25, 'z':26 }
    String = list(s)
    
    for i in range(0,len(String)-1):
        j=i+1
        if String[i] != String[j]:
            WeightedString.append(String[i])
            WeightedString.append(String[i])
        else:
            while String[i] != String[j]:
                WeightedString.append(' '.join(String[i:j]))
                j+=1
        
            
    for s in WeightedString:
        if len(a) == 1:
            if alpha[a] == x:
                return 'Yes'
            else:
                return 'No'
        else:
            add = 0
            for element in a:
                add+=alpha[element]
            if add == x:
                return 'Yes'
            else:
                return 'No'
            
            
    
    
    
    

s = raw_input().strip()
n = int(raw_input().strip())

for a0 in xrange(n):
    x = int(raw_input().strip())
    print CheckWeighted(x,s)
