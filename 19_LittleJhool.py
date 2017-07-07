def main():
    binary = [ 0 , 1 ]
    binary_input = []
    previous = 0
    b = raw_input()
    six_consecutive = 1
    binary_input=map(int,list(b))
    for i in range(0,len(binary_input)):        
        if i == 0:
            previous = binary_input[i] # initialization
            six_consecutive = six_consecutive + 1
            
        else:
            if previous == binary_input[i]:
                six_consecutive = six_consecutive + 1
            elif six_consecutive > 0:
                six_consecutive = 1
                
            previous = binary_input[i]
            if six_consecutive == 6:
                print 'Sorry, sorry!'
                break
            
    if six_consecutive < 6:
        print "Good luck!" 


                
   
if __name__ == '__main__':
    main()  
