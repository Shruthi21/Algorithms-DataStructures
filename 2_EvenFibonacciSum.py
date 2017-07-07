#Even Fibonacci numbers
def SumEvenFibonacci(n):
    firstNum = 1
    secondNum = 1
    FibonacciNum = 0
    SumEven = 0
 
    while FibonacciNum<=n:
        
        FibonacciNum = secondNum + firstNum        
        firstNum = secondNum
        secondNum = FibonacciNum
        
        if FibonacciNum % 2 == 0:
            SumEven+=FibonacciNum
            

    return SumEven


if __name__ == '__main__':
    print SumEvenFibonacci(4000000) 
        
