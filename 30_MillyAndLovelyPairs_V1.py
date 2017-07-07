T = int(raw_input())
cute_list = []
cute_len = 0
max_cute = 0
min_cute = 0
result = []
exp = 0
act = 0
op1 = 0
while T != 0:
    count = 0
    T = T - 1
    N = int(raw_input())
    C = raw_input()
    cute_list = map(int,C.split())
    if len(cute_list) == N:
        cute_len = len(cute_list)
        copy_cute = cute_list
        max_cute = max(cute_list)
        min_cute = min(cute_list)
        act = max_cute - min_cute
        del copy_cute[copy_cute.index(max_cute)]
        del copy_cute[copy_cute.index(min_cute)]
                
        while copy_cute != []:
            max_cute = max(cute_list)
            min_cute = min(cute_list)
            exp = max_cute - min_cute
            if exp == act:
                count = count + 1
            del copy_cute[copy_cute.index(max_cute)]
            del copy_cute[copy_cute.index(min_cute)]

       
        result.append(count)


for r in result:
    print r
            
