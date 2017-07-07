def best_move(player_val, A):
    Me_player = []
    Opponet_player = []
    length = len(A)
    if length!= len(A[0]):
        return False
    for i in range(0,length):
        for j in range(0,length):
            if A[i][j] == player_val:
                Me_player.append([i,j])
            elif A[i][j] != 0 and A[i][j] != -1:
                Opponet_player.append([i,j])
    print Me_player
    print Opponet_player

                


def all_path(xy,A):
    all_path = []
    path = []
    
    x= xy[0]
    y= xy[1]
    max_rowscolumn = 9
    min_rowscolumn = 0
    path.append(xy)
    while x >=min_rowscolumn:        
        
        x = x-1
        if A[x][y] != 0:
            print 'break'
            print path
            print [x,y]
            break
            
        else:
            path.append([x,y])
            print [x,y]
    
    if path != []:
        all_path.append(path)
    path = []
    
    path.append(xy)  
    while x <=max_rowscolumn and x >= 0:
               
        x = x + 1
        print x
        print y
        if A[x][y] != 0:
            print 'break'
            print path
            print [x,y]
        else:
            path.append([x,y])
            print [x,y]
    if path != []:
        all_path.append(path)
    path = []
    
    path.append(xy)
    while y >=min_rowscolumn: 
                
        y = y-1
        if A[x][y] != 0:
            print 'break'
            print path
            print [x,y]
        else:
            path.append([x,y])
            print [x,y]

    if path != []:
        all_path.append(path)
    path = []
     
    path.append(xy)     
    while y <=max_rowscolumn and y >= 0:           
        y = y-1
        if A[x][y] != 0:
            print 'break'
            print path
            print [x,y]
        else:
            path.append([x,y])
            print [x,y]
    if path != []:
        all_path.append(path)
    
    return all_path
    
    




















            
