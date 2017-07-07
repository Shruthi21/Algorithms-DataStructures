binary = []
testcase = int(raw_input())

result = []
while testcase != 0:
    count = 0
    number = int(raw_input())
    binary = list(bin(number))        
    for b in binary:
    	if b == '1':
            		count = count + 1
    result.append(count)
    testcase = testcase - 1
for r in result:
    print r
