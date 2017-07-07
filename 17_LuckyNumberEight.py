#!/bin/python

import sys
def LuckyNumberEight(number,n):
    string_number = str(number)
    list_number=[]
    list_number.append(number)
    for element in string_number:
        list_number.append(int(element))

    for i in range(0,n+1):
        for j in range(0,n+1):
            if i!=j and i<=j:
                if int(string_number[i:j]) not in list_number:
                    list_number.append(int(string_number[i:j]))
                    
            
    
    print list_number
    print len(list_number)
    counter = 0
    for num in list_number:
        if (num%8) == 0:
            print 'divisible'
            print num
            counter+=1
    return counter

if __name__ == '__main__':
    n = int(raw_input().strip())
    number = raw_input().strip()
    result = 0
    if len(number) == n:
        result = LuckyNumberEight(int(number),n)
        print (result%(pow(10,9)+7))
