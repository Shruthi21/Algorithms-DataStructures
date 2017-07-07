#Rotate an array of n elements to the right by k steps
#For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#How many different ways do you know to solve this problem?


def rotate_right(A,k):
    A_rev=[]
    k_counter = k
    read_index= len(A)-1
    while k_counter !=0:
        A_rev.insert(0, A[read_index])    
        k_counter = k_counter - 1
        read_index = read_index - 1

    for i in range(0,read_index+1):
        A_rev.append(A[i])

    return A_rev



        
    
    
    
    
