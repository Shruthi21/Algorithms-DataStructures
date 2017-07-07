# Enter your code here. Read input from STDIN. Print output to STDOUT
def diff():
    
    T = int(raw_input())
    max_int = 0
    diff = 0 
    min_result = []
    int_array = map(int,raw_input().split())
    if len(int_array) == T:
        Q = int(raw_input())
        while Q != 0:
            Q = Q - 1
            result = []
            
            Queries = map(int,raw_input().split())            
            for i in xrange(Queries[0],Queries[1]+1):
                for j in xrange(i+1,Queries[1]+1):
                    diff = (int_array[i] - int_array[j])
                    if max_int == 0:
                        max_int = diff
                    elif  max_int < diff:
                        max_int = diff

            
            print max_int
            max_int = 0
            del(Queries)            
            
            
                
    

        
        
if __name__ == '__main__':
    diff() 
                    
                    
