words = raw_input()
palin = ''
word_len = len(words)
if word_len <= 100 and word_len >= 1:
    while word_len != 0:
        palin = palin +  words[word_len-1]
        word_len = word_len - 1
if palin == words:
    print 'YES'
else:
    print 'NO'
    
        
