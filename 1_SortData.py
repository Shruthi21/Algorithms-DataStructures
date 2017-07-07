#!/bin/python
def displayPathtoPrincess(n,grid):
    bot_pos =[]
    princess_pos = []
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'p':
                princess_pos = [i, j]            
            if grid[i][j] == 'm':
                bot_pos = [i,j]



    if len(bot_pos) == len(princess_pos) == 2:
        if bot_pos[0] > princess_pos[0]:
            print 'UP'
            if bot_pos[1] > princess_pos[1]:
                print 'LEFT'
            else:
                print 'RIGHT'
        else:
            print 'DOWN'
            if bot_pos[1] > princess_pos[1]:
                print 'LEFT'
            else:
                print 'RIGHT'
          
                

if __name__ == '__main__':
    T = int(raw_input())
    grid = []
    n = T
    while T != 0:
        T = T-1
        grid.append(list(raw_input()))
    
    displayPathtoPrincess(n,grid)       

    
