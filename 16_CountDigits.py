def main():
    num = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    string = list(map(int,raw_input()))
    for s in string:
        num[s] = num[s] + 1  
       
    
    for i in range(0,10):
        print str(i) + " " + str(num[i])
        
        
    
if __name__ == '__main__':
    main()  
