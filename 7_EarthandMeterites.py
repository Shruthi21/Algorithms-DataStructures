def create_matrix(N,M):
    return [[0 for x in range(N)] for x in range(M)]    

def split_matrix(Matrix,x,y):
    Matrix[y-1][x-1] = 1    
    return Matrix

def mark_matrix(Matrix,x,y):
    for i in range(0, len(Matrix)):
        if Matrix[i][x-1] == 0:
            Matrix[i][x-1] = 2
    for i in  range(0, len(Matrix)):
        if Matrix[y-1][i] == 0:
            Matrix[y-1][i] = 2
       
    
def calculate_region(matrix):
    area_of_region = []
    area = 0
    print len(matrix)
    print len(matrix[0])
    start_pos = [0,0]
    
    for i in range(0,len(matrix)):
        print i
        for j in range(0, len(matrix)):
            print j
            
            if matrix[i][j] == 0:
                print matrix[i][j]
                if start_pos != [i,j]:
                    start_pos = [i,j]
                    while i >= 0 and i < len(matrix)-1:
                        i = i + 1
                        print i
                        print j
                        if matrix[i][j] == 0:
                            area = area + 1
                    while j >= 0 and j<len(matrix[0])-1:
                        j = j + 1
                        if matrix[i][j] == 0:
                            area = area + 1
                      
                area = area + 1
            else:
                area_of_region.append(area)
                    
                    
                    
    print area_of_region                
            
            
            

    
           
    
def main():
    result = 0
    matrix = []
    T =int(raw_input())
    if T > 10 and T < 0:
        print 'Invalid testcases'
    else:
        while T != 0:
            if T <= 10:
                N = long(raw_input())
                M = long(raw_input())
                if N >= 2 and M <= 10**5:
                    matrix = create_matrix(N,M)
                    print matrix
                    Q = int(raw_input())
                    if Q>0 and Q<= 10 ** 5:
                        while Q!=0:
                            x = long(raw_input())
                            y = long(raw_input())
                            split_matrix(matrix, x, y)
                            print matrix
                            mark_matrix(matrix, x, y)
                            print matrix      
                            
                            Q = Q - 1
                            
            T = T - 1                
                    
        calculate_region(matrix)
                
    
if __name__ == '__main__':
    main()  
