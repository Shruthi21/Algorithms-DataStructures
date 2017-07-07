comb = []

def reverse_list(reverse):
    return  reverse[::-1]
    
    

def append_list(append_list):
    if append_list not in comb and reverse_list(append_list) not in comb:
        comb.append(append_list)
    return comb

def main():
    TC = []
    coder1 = []
    coder2 =[]
    count = 0
    ab = []
    comb = []
    count_list = []
    flag = 0
    
    T =int(raw_input())
    if T != ' ' and T <= 10:
        while T!= 0:
            count = 0
            
            TC = raw_input().split()
            if len(TC) == 2:
                i = 1
                while i <= int(TC[0]):
                    coder1.append(i)
                    coder2.append(i)
                    i = i + 1
            
                P = int(TC[1])
                j = 0
                while j != P:
                    ab.append(raw_input().split())  
                    j = j + 1
                    

                
                for code1 in coder1:
                    for code2 in coder2:
                                               
                        comb = append_list([code1, code2])
                        
     
                        
                
                for each in comb:
                    
                    if each[0] == each[1]:
                        count = count + 1

                    else:

                        for a in ab:                                
                            if int(a[0]) in each and int(a[1]) in each:                                

                                flag = 0
                                break
                            else:
                                flag = 1
                                

                        if flag == 1:
                            count = count + 1

                count_list.append(count)
            T = T - 1
    for c in count_list:
        print c
    
        
if __name__ == '__main__':
    main() 
