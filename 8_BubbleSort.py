import time
def BubbleSort(Array):
    startTime = time.time()
    
    for i in range(0,len(Array)):
        for j in range(i+1, len(Array)):
            if Array[i] > Array[j]:
                Array[i], Array[j] = Array[j], Array[i]
                
    
    
    print time.time() - startTime
    return Array
