def sum_of_squares(num):
    i = 0
    SumFirstSquare = 0
    SquareFirstSum = 0
    for i in range(1,num+1):
        SumFirstSquare = SumFirstSquare + i
        SquareFirstSum = SquareFirstSum + (i * i)

       
    SumFirstSquare = SumFirstSquare * SumFirstSquare
    return (SumFirstSquare - SquareFirstSum)
    
    
