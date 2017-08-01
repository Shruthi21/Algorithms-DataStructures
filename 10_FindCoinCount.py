##Given a value N, if we want to make change for N cents,
##and we have infinite supply of each of S = { S1, S2,...
##. , Sm} valued coins, how many ways can we make the
##change? The order of coins doesn’t matter.
##
##For example, for N = 4 and S = {1,2,3}, there are four
##solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output
##should be 4. For N = 10 and S = {2, 5, 3, 6}, there
##are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6},
##{2,3,5} and {5,5}. So the output should be 5.


def FindCoinCount1(S,n):
    table = [[0 for x in range(len(S))] for x in range(n+1)]
    print table

    for i in range(len(S)):
        table[0][i] = 1

    print table
    for i in range(1, n+1):
        for j in range(len(S)):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
    print table
    return table[n][len(S)-1]


def FindCoinCount2(S, m, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0

    return count2(S, m-1, n) + count2(S,m,n-S[m-1])




    
            
        

                    




    

