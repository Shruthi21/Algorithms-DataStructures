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
        print Comb
        if Comb != '' and Comb != '[...]':
            for i in range(0,len(rgb)):
                if UserRgb[i] != 0:
                    if rgb[i] in Comb:
                        if UserRgb[i] > 1:
                            count = 0
                            j = 0
                            while j > 0:
                                
                                j = Comb.find(rgb[i],j,len(Comb))
                                count+=1

                            if count == UserRgb[i]:
                                if Comb not in ResultComb:
                                    ResultComb.append(Comb)
                                    print ResultComb
                                    print 'occurence more than one'
                                    print Comb
                           
                       
                        elif UserRgb[i] == 1:
                            if Comb not in ResultComb:
                                ResultComb.append(Comb)
                                print ResultComb
                                print 'occurence once'
                                print Comb
                                
            
    for i in range(0,len(rgb)):
        for res in ResultComb:        
            print rgb[i]
            print res
            if UserRgb[i] == 0:
                if rgb[i] in res:
                    print 'deleted'
                    print res                    
                    ResultComb.remove(res)
                    
                
    
    print len(ResultComb)
    print len(AllComb)
    return ResultComb
     
           
    

if __name__ == '__main__':
      
    UserRgb = []
    n = int(raw_input().strip())
    AllComb = CalculateAllCombination(n)
                
    

    i = 6
    CombValue = 0
    while i != 0:
        i-=1
        CombValue = int(raw_input())
        UserRgb.append(CombValue)

    print UserRgb
    print CalculateFlower(AllComb,UserRgb)

    




    
    
        
        
    








