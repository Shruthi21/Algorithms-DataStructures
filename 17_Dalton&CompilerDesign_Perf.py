def main():
    n = int(raw_input())
    while n != 0:
        n = n - 1
        strength = int(raw_input())
        divide_result = strength/2
        if strength % 2 == 0:
            print str(divide_result) + ' ' + str(divide_result)
        else:
            print str(divide_result) + ' ' + str(divide_result + 1)        
       
        
    
if __name__ == '__main__':
    main()  
