import sys
import os

def sum(num):
    sum_num = 0
    for n in num:
        sum_num = sum_num + n

    return sum_num
        
f = open(os.environ['OUTPUT_PATH'],'w')

_numbers_cnt = 0
_numbers_cnt = int(raw_input())
_numbers_i=0
_numbers= []
while _numbers_i < _numbers_cnt:
    _numbers_item = int(raw_input())
    _numbers.append(_numbers_item)
    _numbers_i+= 1

res = sum(_numbers)
f.write(str(res) +"\n")
f.close()
