def abbreviate(sentence):
    acronym  = ''
    sen_list = sentence.split()
    for s in sen_list:
        acronym = acronym + s[0]       
      
    return acronym.upper()
