#!/bin/python
def nextMove(n,r,c,grid):    
    princess_pos = []
    bot_pos = [r,c]
    result_list = ''
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'p':
                princess_pos = [i, j]    
    
    if len(bot_pos) == len(princess_pos) == 2:
        if bot_pos[0] > princess_pos[0]:
            return 'UP '
        elif bot_pos[0] < princess_pos[0]:
            return 'DOWN'
            

        
        if bot_pos[1] > princess_pos[1]:
            return 'LEFT'
        elif bot_pos[1] < princess_pos[1]:
            return 'RIGHT'


   


n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
