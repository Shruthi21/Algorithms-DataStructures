def main():
    dict_direction = { 'L': -1,'R': 1,'D': -1, 'U':1 }
    direction = list(raw_input())
    start_position = [0,0]
    for d in direction:
        if d == 'L' or d == 'R':
            start_position[0] = start_position[0] + (dict_direction[d])
        else:
            start_position[1] = start_position[1] + (dict_direction[d])
    print str(start_position[0]) + ' ' + str(start_position[1])        
            
        
                
   
if __name__ == '__main__':
    main()  
