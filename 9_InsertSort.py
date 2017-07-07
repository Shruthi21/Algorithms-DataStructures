import time
def InsertSort(Array):
    startTime = time.time()

    for i in range(1,len(Array)):
        value = Array[i]
        index = i - 1
        while index >= 0 and Array[index] > value:
            Array[index], Array[index + 1] = Array[index + 1], Array[index]
            index = index - 1


    print time.time() - startTime
    return Array    
