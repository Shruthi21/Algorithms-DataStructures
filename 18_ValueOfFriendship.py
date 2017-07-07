#!/bin/python

import sys



def FindValue(n,m,x,y,DictFriends):

    Result = 0

    if x not in DictFriends[y]:
        DictFriends[y].append(x)
    if y not in DictFriends[x]:
        DictFriends[x].append(y)


    for e1 in DictFriends[y]:
        if e1 != x:
            if e1 not in DictFriends[x]:
                DictFriends[x].append(e1)
            if x not in DictFriends[e1]:
                DictFriends[e1].append(x)                        
    for e2 in DictFriends[x]:
        if e2 != y:
            if e2 not in DictFriends[y]:
                DictFriends[y].append(e2)
            if y not in DictFriends[e2]:
                DictFriends[e2].append(y) 
                          

    Sum= 0
    for i in range(1,n+1):
        Sum+=len(DictFriends[i])

    
    Result+=Sum
    return Result
        
    
    
if __name__ == '__main__':
    t = int(raw_input().strip())
    Total = 0
    DictFriends = {}
    for a0 in xrange(t):
        n,m = raw_input().strip().split(' ')
        n,m = [int(n),int(m)]
        for i in range(1,n+1):
            DictFriends[i] = list()        
        for a1 in xrange(m):
            x,y = raw_input().strip().split(' ')
            x,y = [int(x),int(y)]
            # your code goes here
            
            Total+= FindValue(n,m,x,y,DictFriends)
    print Total

