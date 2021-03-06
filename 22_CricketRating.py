#https://en.wikipedia.org/wiki/Maximum_subarray_problem

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main():
    score = []
    highest_score = 0
    avg = 0    
    N = int(raw_input())
    if N == 0:
        print N
    else:
        score = map(int,raw_input().split())
        if len(score) == N:
            print max_subarray(score)
        
        

                
   
if __name__ == '__main__':
    main()  
