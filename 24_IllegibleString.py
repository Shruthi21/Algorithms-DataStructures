def main():
    pos = 0
    list_string = []
    short_string = ''
    long_string = ''
    result_string = ''
    N = int(raw_input())
    string = raw_input().upper()
    
    count  = 0
    if len(string) == N:
        list_string = list(string)
        for i in range(0,len(list_string)):
            if list_string[i] == 'W':
                short_string = short_string + 'W'
                long_string = long_string + 'V'
                long_string = long_string + 'V'             
                
                
                
            elif list_string[i] == 'V':
                count = count + 1
                
                if count == 2:
                    long_string = long_string + 'V'
                    long_string = long_string + 'V' 
                    short_string = short_string + 'W'
                    count = 0

                    
                    
            else:
                short_string = short_string + list_string[i]
                long_string = long_string + list_string[i]
                
                
    if count == 1:
        long_string = long_string + 'V'
        short_string = short_string + 'W'
        
    
    result_string = str(len(short_string)) + ' ' + str(len(long_string))
    print result_string              
  
                
        
                
   
if __name__ == '__main__':
    main()  
