m_n = map(int,raw_input().split())
transpose_list = []
after_transpose =  [[]]

m = m_n[0]
n = m_n[1]
while m != 0:
    m = m - 1
    transpose = map(int, raw_input().split())
    if len(transpose) == n:
        transpose_list.append(transpose)  

x= len(transpose_list)
y = len(transpose_list[0])

after_transpose = [[[] for _ in xrange(x)] for _ in xrange(y)]


for i in range(0,len(transpose_list)):
    for j in range(0,len(transpose_list[0])):        
        after_transpose[j][i] = transpose_list[i][j]
        
        

for i in range(len(after_transpose)):
    string = ''
    for j in range(0, len(after_transpose[0])):
        string = string + ' ' + str(after_transpose[i][j])
        
    print string
	
    
