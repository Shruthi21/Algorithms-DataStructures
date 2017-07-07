def main():
    t = int(raw_input())
    disliked_words = []
    result = []
    A = ''
    print_result = ''
    while t != 0:
        t = t - 1
        disliked_words.append(raw_input().upper())
        
    no_of_words = int(raw_input())
    acronym = raw_input().split()
    print acronym
    for a in acronym:
        A = a.upper()
        if A not in disliked_words:
            result.append(A[0])
            
    for i in range(0,len(result)):
        if i == 0:
            print_result = print_result + result[i]
        else:
            print_result = print_result + '.' + result[i]

    print print_result        
    
                
   
if __name__ == '__main__':
    main()  
