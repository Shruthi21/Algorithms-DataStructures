def minsum(X,Y,N):
    total = 0
    summ = 999999999
    for i in range(1,N):
        for j in range(1,N):
            if i != j:
                total = X[i] + Y[j];
                if summ > total:
                    sum=total;
    return summ

    


X = []
Y = []
abc = map(int,raw_input().split())
N = int(raw_input())
if len(abc) == 3:
	a = abc[0]
	b = abc[1]
	c = abc[2]

X.append(a * c)
print X
for i in range(1,N):
    X[i].append(( X[i-1] * a * b * c ) + ( X[i-1] * a * b ) + (X[i-1] * a * c))
    X[i].append( X[i] % 1000000007 )

Y.append(b * c)
for i in range(1, N):
    Y[i].append((Y[i-1] * b * c * a ) + (Y[i-1] * b * a) + (Y[i-1] * b * c))
    Y[i].append(Y[i] % 1000000007)

print minsum(X,Y,N)   
   	
   	
