def number_needed(a, b):
    a_list = sorted(a)
    b_list = sorted(b)
    deletions = 0

    print a_list
    print b_list
    print len(a_list)
    print len(b_list)
    if len(a_list) != 0 or len(b_list)!= 0:
        if len(a_list) == len(b_list):
            for ele in a_list:
                if ele not in b_list:
                    deletions+=1

            for ele in b_list:
                if ele not in a_list:
                    deletions+=1
                    
        elif len(a_list) > len(b_list):
            for i in range(0,len(a_list)+1):
                if i < len(b_list):
                    if a_list[i] != b_list[i]:
                        
                        deletions+=1
                        

            
        elif len(a_list) < len(b_list):
            for i in range(0,len(b_list)):
                if i < len(a_list):
                    if a_list[i] != b_list[i]:
                        print b_list[i]
                        del(b_list[i])
                        deletions+=1
                        print b_list
                        print b_list[i]

            print b_list
            print len(b_list)
            print len(a_list)

        

            
    else:
        deletions = len(a_list)+len(b_list)        
    

                    
    return deletions

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
