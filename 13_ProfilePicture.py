dimension = int(raw_input())
test_case = int(raw_input())
length_width = []
print_result = {0:'CROP IT', 1:'UPLOAD ANOTHER', 2:'ACCEPTED'}
result = []
while test_case != 0:
    length_width = map(int, raw_input().split())
    
    if len(length_width) == 2:
        if length_width[0] == length_width[1] and length_width[0] >= dimension:
            result.append(2)
        elif length_width[0] < dimension or length_width[1] < dimension:
            result.append(1)
        elif length_width[0] > dimension or length_width[1] > dimension:
            result.append(0)
    test_case = test_case - 1

                    
           
for r in result:
    print print_result[r]
