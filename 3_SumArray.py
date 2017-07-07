def SumArray():
    n = int(raw_input())
    int_array = []
    sum_num = 0
    while n!= 0:
        n = n - 1
        int_array.append(int(raw_input()))

    for num in int_array:
        sum_num = sum_num + num

    print sum_num
        

if __name__ == '__main__':
    SumArray()  
