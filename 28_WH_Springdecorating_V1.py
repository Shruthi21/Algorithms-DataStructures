#!/bin/python

import sys

# your code goes here 
    
RgbList = []


def CalculateAllCombination(n):
    Set = [ 'R','G','B']
    return CalculateN(Set, "", len(Set), n)

def CalculateN(Set,prefix,k,n):
    
    RbgString = ''
    

    if n == 0:
        if prefix != '':
            return prefix
    else:
        for i in range(0,k):
            NewPrefix = prefix + Set[i]
            RbgString = CalculateN(Set,NewPrefix,k,n-1)
            if RbgString not in RgbList and RgbList != '':
                RgbList.append(RbgString)
    return RgbList

def CalculateFlower(AllComb,UserRgb):
    rgb = ['RB','RG','BR','BG','GR','GB']
    ResultComb = []
    
    for Comb in AllComb:
        all_same = 1
        c0=Comb[0]
        cLength = len(Comb)
        while cLength != 0:
            cLength-=1
            if Comb[cLength] != c0:
                all_same = 0
                exit
            
        if  all_same == 1:
            if Comb not in ResultComb:
                ResultComb.append(Comb)    
            
            
            
        


                
        
        if Comb != '' and Comb != '[...]':
            for i in range(0,len(rgb)):
                if UserRgb[i] != 0:
                    if rgb[i] in Comb:
                        if Comb not in ResultComb:
                            ResultComb.append(Comb)

                                
            
    for i in range(0,len(rgb)):
        for j in range((len(ResultComb)-1),0,-1):      
            
            if UserRgb[i] == 0:
                if rgb[i] in ResultComb[j]:           
                    del ResultComb[j]

    
                
    
    return ResultComb
     
           
    

if __name__ == '__main__':
      
    UserRgb = []
    n = int(raw_input().strip())
    AllComb = CalculateAllCombination(n)
    Result = []           
    

    i = 6
    CombValue = 0
    while i != 0:
        i-=1
        CombValue = int(raw_input())
        UserRgb.append(CombValue)

    Result = CalculateFlower(AllComb,UserRgb)
    print Result
    print len(Result)
    

    




    
    
        
        
    








