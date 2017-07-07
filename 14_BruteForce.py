def main():
    num = int(raw_input())
    fac = 1
    if num <= 10 and num >= 1:
        while num != 0:
            fac = fac * num
            num = num - 1
    print fac    
        
        
    
if __name__ == '__main__':
    main()  
