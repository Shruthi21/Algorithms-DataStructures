#!/bin/python

import sys

def RoundGrades(Grades):
    Result = []
    for g in Grades:
        # first condition
        Round = g
        while (Round%5)!= 0:
            Round+=1
            

        
        # second conditon
        if g>=38 and g<=38:
            g=40
            Result.append(g)
            
        elif g < 38:
            Result.append(g)            
            
        elif (Round - g) <= 3:
            Result.append(Round)
                        
        

        else:
            Result.append(g)
        
    return Result        

n = int(raw_input().strip())
Grades = []
Result = []
for a0 in xrange(n):
    grade = int(raw_input().strip())
    Grades.append(grade)
    # your code goes here
Result = RoundGrades(Grades)
for r in Result:
    print r
