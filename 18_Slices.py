def slices(num_string, num):
    num_list = list(num_string)
    
    merged_slice = []
    len_num = len(num_list)
    i = 0
    if len_num >= num:
        while i<= len_num:
            if len(num_list[i:i+num]) == num:
                merged_slice.append(map(int,(num_list[i:i+num])))                
            i = i+1

    else:
        return 'Invalid input'        
    
    
    return merged_slice
    
        
        
