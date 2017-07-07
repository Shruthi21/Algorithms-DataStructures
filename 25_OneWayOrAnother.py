def MaxMin(list_r_c_x):
    max_limit = 0
    min_limit = 1
    for r_c_x in list_r_c_x:
        if max(r_c_x[0],r_c_x[1]) > max_limit:
            max_limit =  max(r_c_x[0],r_c_x[1])
            
        if min_limit != 0 and  min(r_c_x[0],r_c_x[1]) < min_limit:
            min_limit = min(r_c_x[0],r_c_x[1])
            
    return max_limit, min_limit

def Check(dict_r_c_x,mini,maxi,possible):
    
    for i in range(mini,maxi):
        for j in range(mini,maxi):
            if (i,j) in dict_r_c_x:
                if (i+1,j) in dict_r_c_x:
                    if dict_r_c_x[(i,j)] == 'E' and dict_r_c_x[(i + 1,j)] == 'E':
                        possible = 'No'
                elif (i,j+1) in dict_r_c_x:
                    if dict_r_c_x[(i,j)] == 'E' and dict_r_c_x[(i,j + 1)] == 'E':
                        possible = 'No'                
    return possible            
        

def x_axis_check(dict_r_c_x, r_c_x, sign):
    possible = 'Yes'
    if sign == '+':
        if (r_c_x[0], r_c_x[1]) in dict_r_c_x:
            r = r_c_x[0] + 1
            if (r, r_c_x[1]) not in dict_r_c_x:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E':
                    dict_r_c_x[(r, r_c_x[1])] = 'O'
                else:
                    dict_r_c_x[(r, r_c_x[1])] = 'E'
            else:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E' and dict_r_c_x[(r, r_c_x[1])] == 'E':
                    possible = 'No'
                
    else:
        if (r_c_x[0], r_c_x[1]) in dict_r_c_x:
            r = r_c_x[0] - 1
            if (r, r_c_x[1]) not in dict_r_c_x:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E':
                    dict_r_c_x[(r, r_c_x[1])] = 'O'
                else:
                    dict_r_c_x[(r, r_c_x[1])] = 'E'
            else:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E' and dict_r_c_x[(r, r_c_x[1])] == 'E':
                    possible = 'No'

    return possible


def y_axis_check(dict_r_c_x, r_c_x, sign):
    possible = 'Yes'
    if sign == '+':
        if (r_c_x[0], r_c_x[1]) in dict_r_c_x:
            r = r_c_x[1] + 1
            if (r_c_x[0], r) not in dict_r_c_x:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E':
                    dict_r_c_x[(r_c_x[0], r)] = 'O'
                else:
                    dict_r_c_x[(r_c_x[0], r)] = 'E'
            else:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E' and dict_r_c_x[(r_c_x[0], r)] == 'E':
                    possible = 'No'
                
    else:
        if (r_c_x[0], r_c_x[1]) in dict_r_c_x:
            r = r_c_x[1] - 1
            if  (r_c_x[0], r) not in dict_r_c_x:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E':
                    dict_r_c_x[(r_c_x[0], r)] = 'O'
                else:
                    dict_r_c_x[(r_c_x[0], r)] = 'E'
            else:
                if dict_r_c_x[(r_c_x[0], r_c_x[1])] == 'E' and dict_r_c_x[(r_c_x[0], r)] == 'E':
                    possible = 'No'

    return possible 

def OneWayOrAnother():
    T = int(raw_input())
    possible = 'Yes'
    while T != 0:
        T = T - 1
        N = int(raw_input())
        r_c_x = []
        list_r_c_x = []
        dict_r_c_x = {}        
        while N != 0:
            N = N - 1
            r_c_x = map(int,raw_input().split())
            if len(r_c_x) == 3:
                if r_c_x[2]%2 == 0:
                    dict_r_c_x[(r_c_x[0], r_c_x[1])]  = 'E'
                else:
                    dict_r_c_x[(r_c_x[0], r_c_x[1])] = 'O'                
                list_r_c_x.append(r_c_x)
                
        maxi,mini = MaxMin(list_r_c_x)
        print maxi
        print mini
        print list_r_c_x
        print dict_r_c_x
        for i in range(mini,maxi):
            for j in range(mini,maxi):
                print i
                print j
                if (i,j) in dict_r_c_x:
                    if dict_r_c_x[(i,j)] == 'E':
                        if (i + 1,j) not in dict_r_c_x:
                            dict_r_c_x[(i + 1,j)] = 'O'
                        elif dict_r_c_x[(i + 1,j)] != 'O':
                            possible = 'No'
                            break                     
                            
                        if (i,j + 1) not in dict_r_c_x:
                            dict_r_c_x[(i,j + 1)] = 'O'
                        elif dict_r_c_x[(i,j + 1)] != 'O':
                            possible = 'No'
                            break
                        
                    else:
                        if (i + 1,j) not in dict_r_c_x:
                            dict_r_c_x[(i + 1,j)] = 'E'
                        elif dict_r_c_x[(i + 1,j)] != 'E':
                             possible = 'No'
                             break
                            
                        if (i,j + 1) not in dict_r_c_x:
                            dict_r_c_x[(i,j + 1)] = 'E'
                        elif dict_r_c_x[(i,j + 1)] != 'E':
                            possible = 'No'
                            break
                        
                      
                else:#when the r,c not in dictionary
                    if (i + 1,j) in dict_r_c_x:
                        if dict_r_c_x[(i + 1,j)] == 'E':
                            dict_r_c_x[(i,j)] = 'O'
                        else:
                            dict_r_c_x[(i,j)] = 'E'
                    elif (i,j + 1) in dict_r_c_x:        
                        if dict_r_c_x[(i,j + 1)] == 'E':
                            dict_r_c_x[(i,j)] = 'O'
                        else:
                            dict_r_c_x[(i,j)] = 'E'
                    
            
        
        print dict_r_c_x
        print Check(dict_r_c_x, mini,maxi,possible)   


if __name__ == '__main__':
    OneWayOrAnother()
    
                             
            

                
            
            

