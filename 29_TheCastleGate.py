T = int(raw_input())
result = []
while T != 0:
    count = 0
    T = T - 1
    N = int(raw_input())
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i ^ j <= N:
                count = count + 1
        
    result.append(count)
    
for r in result:
    print r
