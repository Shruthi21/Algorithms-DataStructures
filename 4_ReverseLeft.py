#Arrays: Left Rotation

def array_left_rotation(a, n, k):
    RevLeft=[]
    KCounter = k
    ReadIndex = 0
    while KCounter != 0:
        RevLeft.insert(n-1,a[ReadIndex])
        KCounter = KCounter - 1
        ReadIndex = ReadIndex + 1

    for i in range(n-1,ReadIndex-1,-1):
        RevLeft.insert(0,a[i])

    return RevLeft    
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
