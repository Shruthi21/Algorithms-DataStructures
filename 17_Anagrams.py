def detect_anagrams(word, sentence):
    anagram_list = []
    i = 0
    word_list = list(word)    
    for every_word in sentence:
        if every_word == word:
            break
        if len(word) == len(every_word):
            for i in range(0,len(word_list)):
                if word_list[i] in every_word:
                    if i == len(word_list)-1:                        
                        anagram_list.append(every_word)
                        
                else:
                    break                 

                    
    return anagram_list                
                    
    
    

