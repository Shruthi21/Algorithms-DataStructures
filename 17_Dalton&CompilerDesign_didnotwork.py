def main():
    divide_result = 0
    test_case = int(raw_input())
    if test_case >= 1 and test_case <= 100000:
        while test_case != 0:
            test_case = test_case - 1
            strength = int(raw_input())
            if strength >= 1 and strength <= 100000:
                divide_result = strength/2
                if strength % 2 == 0:
                    print str(divide_result) + ' ' + str(divide_result)
                else:
                    print str(divide_result) + ' ' + str(divide_result + 1)        
       
        
    
if __name__ == '__main__':
    main()  
