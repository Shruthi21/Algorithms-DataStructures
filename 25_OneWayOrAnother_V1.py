def Check(dict_r_c_x,r,c):
    possible = 'Yes'
    last = dict_r_c_x[(r[0],r[1])]
    start_pos = r[0]
    end_pos = c[0]
    if start_pos > end_pos:
        while start_pos != end_pos:
            start_pos = start_pos - 1
            if (start_pos, r[1]) not in dict_r_c_x:
                if last == 'E':
                    dict_r_c_x[(start_pos, r[1])] = 'O'
                    last = 'O'
                else:
                    dict_r_c_x[(start_pos, r[1])] = 'E'
                    last = 'E'
                      
            else:
                if last == 'E' and dict_r_c_x[(start_pos, r[1])] == 'E':
                    possible = 'No'
                    return possible
                elif last == 'O' and dict_r_c_x[(start_pos, r[1])] == 'O':
                    possible = 'No'
                    return possible
    else:
        while start_pos != end_pos:
            start_pos = start_pos + 1
            if (start_pos, r[1]) not in dict_r_c_x:
                if last == 'E':
                    dict_r_c_x[(start_pos, r[1])] = 'O'
                    last = 'O'
                else:
                    dict_r_c_x[(start_pos, r[1])] = 'E'
                    last = 'E'
                      
            else:
                if last == 'E' and dict_r_c_x[(start_pos, r[1])] == 'E':
                    possible = 'No'
                    return possible
                elif last == 'O' and dict_r_c_x[(start_pos, r[1])] == 'O':
                    possible = 'No'
                    return possible            
             
    start_pos = r[1]
    end_pos = c[1]
    if start_pos > end_pos:
        while start_pos != end_pos:
            start_pos = start_pos - 1
            if (c[0], start_pos) not in dict_r_c_x:
                if last == 'E':
                    dict_r_c_x[(c[0],start_pos)] = 'O'
                    last = 'O'
                else:
                    dict_r_c_x[(c[0], start_pos)] = 'E'
                    last = 'E'
                      
            else:
                if last == 'E' and dict_r_c_x[(c[0], start_pos)] == 'E':
                    possible = 'No'
                    return possible
                elif last == 'O' and dict_r_c_x[(c[0], start_pos)] == 'O':
                    possible = 'No'
                    return possible
    else:
        while start_pos != end_pos:
            start_pos = start_pos + 1
            if (c[0], start_pos) not in dict_r_c_x:
                if last == 'E':
                    dict_r_c_x[(c[0], start_pos)] = 'O'
                    last = 'O'
                else:
                    dict_r_c_x[(c[0], start_pos)] = 'E'
                    last = 'E'
                      
            else:
                if last == 'E' and dict_r_c_x[(c[0], start_pos)] == 'E':
                    possible = 'No'
                    return possible
                elif last == 'O' and dict_r_c_x[(c[0], start_pos)] == 'O':
                    possible = 'No'
                    return possible            
     
        
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

            for i in range(1,len(list_r_c_x)):
                source = [list_r_c_x[i-1][0],list_r_c_x[i-1][1]]
                target = [list_r_c_x[i][0],list_r_c_x[i][1]]
                possible = Check(dict_r_c_x, source, target)

        print possible
           


if __name__ == '__main__':
    OneWayOrAnother()
    
                             
            

                
            
            

