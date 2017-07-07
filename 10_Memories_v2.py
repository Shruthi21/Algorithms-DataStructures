comb = []

def reverse_list(reverse):
    return  reverse[::-1]
    
    

def append_list(append_list):
    if append_list not in comb and reverse_list(append_list) not in comb:
        comb.append(append_list)
    return comb

def generate_coder(N):
    i = 1
    coder = []
    while i <= N:
        coder.append(i)
        i = i + 1
    return coder

  
    

def main():
    TC = []
    coder1 = []
    coder2 =[]
    count = 0
    ab = []
    ba = []
    comb = []
    count_list = []
    flag = 0
    dislike = 0
    
    T =int(raw_input())
    
    if T != ' ' and T <= 10:
        
        while T!= 0:
            count = 0            
            TC = raw_input().split()
            
            
            if len(TC) == 2:
                
                coder1 = generate_coder(int(TC[0]))
                coder2 = generate_coder(int(TC[0]))
                for code1 in coder1:
                    for code2 in coder2:                                               
                        comb = append_list([code1, code2])                       
     

            
                P = int(TC[1])
                j = 0
                count = len(comb)
                while j != P:
                    ab = raw_input().split()
                    
                    for each in comb:
                        if each[0] != each[1]:

                            if int(ab[0]) in each and int(ab[1]) in each:
                                count = count - 1

                                break
                    j = j + 1                           
                count_list.append(count)                
            T = T - 1
    for c in count_list:
        print c
    
        
if __name__ == '__main__':
    main() 
