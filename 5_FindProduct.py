int_array = int(raw_input())
result = 1
array_numbers=[]
array_numbers = map(int,raw_input().split())
if len(array_numbers) == int_array:
    for num in array_numbers:
        result = (result * num) % (pow(10,9) + 7)
print result        
