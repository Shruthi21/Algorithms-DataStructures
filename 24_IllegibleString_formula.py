def main():
    N = int(raw_input())
    string = raw_input().upper()
    w_count = 0
    v_count = 0
    remaining = 0
    len_ss = 0
    len_ls = 0

    if len(string) == N:
        list_string = list(string)
        print list_string
        for i in range(0,len(list_string)):
            if list_string[i] == 'W':
                w_count = w_count + 1         
                
            elif list_string[i] == 'V':
                v_count = v_count + 1
                    
                    
            else:
                remaining = remaining + 1
                
    print v_count
    print w_count
    print remaining
    if v_count + w_count + remaining == N:
        len_ss = w_count + (v_count/2) + remaining
        len_ls = v_count + (w_count * 2) + remaining
        
    
    result_string = str(len_ss) + ' ' + str(len_ls)
    print result_string              
  
                
        
                
   
if __name__ == '__main__':
    main()  
