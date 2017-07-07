#!/bin/python



def CreateChess(n):
    Chess = []
    ChessInner = []
    nTemp = n
    
    while nTemp != 0:
        nTemp-=1
        ChessInner.append(0)

    nTemp = n    
    while nTemp!=0:
        nTemp-=1
        Chess.append(ChessInner)
    return Chess


    


def FindMove(rQueen,cQueen,Obstacle,n,Chess):
    MoveCount = 0
    print rQueen-1
    print cQueen-1
    for i in range(0,n+1):
        for j in range(0,n+1):
            if i == rQueen-1 and j == cQueen-1:
                Chess[i][j] = 1
                
            

    
    print Chess
    rCounter = rQueen
    cCounter = cQueen
    for x_y in Obstacle:
        if Chess[(x_y[0]-1)][(x_y[1]-1)]!= 1:
            Chess[(x_y[0]-1)][(x_y[1]-1)] = 2
    print Chess
    while rCounter!=n:        
        rCounter+=1
        if Chess[rCounter][cCounter] != 1 and Chess[rCounter][cCounter] != 2:
            Chess[rCounter][cCounter] = 3
            MoveCount+=1

    while rCounter!=0: 
        rCounter-=1
        if Chess[rCounter][cCounter] != 1 and Chess[rCounter][cCounter] != 2:
            Chess[rCounter][cCounter] = 3
            MoveCount+=1

    rCounter = rQueen
    while cCounter< n and cCounter!=n:        
        cCounter+=1
        if Chess[rCounter][cCounter] != 1 and Chess[rCounter][cCounter] != 2:
            Chess[rCounter][cCounter] = 3
            MoveCount+=1

    while cCounter> 0 and cCounter!=n:        
        cCounter-=1
        if Chess[rCounter][cCounter] != 1 and Chess[rCounter][cCounter] != 2:
            Chess[rCounter][cCounter] = 3
            MoveCount+=1               
            
    rCounter = rQueen
    cCounter = cQueen
    while rCounter> 0 and cCounter>0:
        cCounter-=1
        rCounter-=1
        if Chess[rCounter][cCounter] != 1 and Chess[rCounter][cCounter] != 2:
            Chess[rCounter][cCounter] = 3
            MoveCount+=1

    rCounter = rQueen
    cCounter = cQueen
    while rCounter< 0 and cCounter<0:
        cCounter+=1
        rCounter+=1
        if Chess[rCounter][cCounter] != 1 and Chess[rCounter][cCounter] != 2:
            Chess[rCounter][cCounter] = 3
            MoveCount+=1


    return MoveCount
            
        
        
    
    
    


if __name__ == '__main__':
    Chess = []
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    rQueen,cQueen = raw_input().strip().split(' ')
    rQueen,cQueen = [int(rQueen),int(cQueen)]
    
    Obstacle = []
    for a0 in xrange(k):
        rObstacle,cObstacle = raw_input().strip().split(' ')
        rObstacle,cObstacle = [int(rObstacle),int(cObstacle)]
        # your code goes here
        Obstacle.append([rObstacle,cObstacle])
    
    print Obstacle
    print rQueen,cQueen
    print n,k
    Chess = CreateChess(n)
    print Chess
    print FindMove(rQueen,cQueen,Obstacle,n, Chess)
