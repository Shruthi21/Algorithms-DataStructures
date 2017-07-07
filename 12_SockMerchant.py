def SockMerchant():
    SockPair = []
    Counter = 0
    
    T = int(raw_input())
    int_array = map(int,raw_input().split())
    if len(int_array) == T:
        for x in int_array:
            if x not in SockPair:
                SockPair.append(x)
            else:
                Counter+=1
                SockPair.remove(x)
                
           
    return Counter            
    

        
        
if __name__ == '__main__':
    print SockMerchant() 
           
