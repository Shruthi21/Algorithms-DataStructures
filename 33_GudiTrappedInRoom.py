def shift(A,n):
    temp = 0
    while n != 0:
        temp = A[len(A)-1]
        A.remove(A[len(A)-1])
        A.insert(0,temp)        
        n = n - 1
    return A

def main():
    T = int(raw_input())
    while T != 0:
        T = T - 1
        string = int(raw_input())



if __name__ == '__main__':
    main() 
