def split_string(source,splitlist):
    result = []
    space = ' '
    split_lsit = []
    
    print source
    for seperator in splitlist:
        for each_string in source.split(seperator):
            print seperator
            print each_string
            if seperator in each_string:                
                new_string = each_string.split(seperator)
                for substring in new_string:            
                    for symbol in substring:
                        if symbol not in list(splitlist):
                            if substring not in result:
                                result.append(substring)
            
                            
                            
                    
            else:
                if each_string not in result:
                    for symbol in each_string:
            
            
                        if symbol in list(splitlist):
                            flag = 1
                            break
                        else:
                            flag = 0
                            
                    if flag == 0:
                        result.append(each_string)
            
            
    
    return result            
                
                
                


   
            





out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
