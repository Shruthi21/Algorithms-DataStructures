T = int(raw_input())
cute_list = []
max_cute = 0
min_cute = 0
result = []
diff = 0
cute_len = 0

while T != 0:
    count = 0
    max_once = 0
    T = T - 1
    N = int(raw_input())
    C = raw_input()
    cute_list = map(int,C.split())
    if len(cute_list) == N:
        cute_len = len(cute_list)
        max_cute = max(cute_list)
        min_cute = min(cute_list)
        while cute_len >= 0:
            cute_len = cute_len - 1
            if cute_list[cute_len] == min_cute:
                count = count + 1


    result.append(count)
    
for r in result:
	print r
