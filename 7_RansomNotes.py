def ransom_note(magazine, ransom):
    for r in ransom:        
        if r not in magazine:            
            return False           
        else:
            magazine.remove(r)

    if ransom != []:
        return True
            
    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
