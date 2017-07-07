def shift_left(A,n):
    temp = 0
    while n != 0:
        temp = A[0]
        A.remove(A[0])
        A.append(temp)        
        n = n - 1
    return A

def shift_right(A,n):
    temp = 0
    while n != 0:
        temp = A[len(A)-1]
        A.remove(A[len(A)-1])
        A.insert(0,temp)        
        n = n - 1
    return A


    
def main():
    oper = 0
    N_M = map(int,raw_input().split())    
    if len(N_M) == 2:
        A = map(int,raw_input().split())
        T = map(int,raw_input().split())
        shifted_list = A
        if len(A) == len(T) == N_M[0]:
            while oper != N_M[1]:            
                oper = oper + 1
                operations = raw_input().split()
                if operations[0] == 'R':
                    shifted_list = shift_right(A, int(operations[1]))
                else:
                    shifted_list = shift_left(A, int(operations[1]))
                    
                if shifted_list == T:                    
                    print oper
                    return

if __name__ == '__main__':
    main() 
