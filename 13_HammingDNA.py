def Hamming(d1,d2):
    d1_list = list(d1)
    d2_list = list(d2)
    hamming_distance = 0
    if len(d1_list) == len(d2_list):
        for i in range(0, len(d1_list)):
            if d1_list[i]!= d2_list[i]:
                hamming_distance = hamming_distance + 1
    return hamming_distance
