def shift_n_letters(letter, n):
    alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26 }
    key_value = alphabet[letter] 
    i = 0
    if n < 0:
        while i!=n:
            if key_value == 1:
                key_value = 26
            else:
                key_value = key_value - 1 
            i = i - 1     
    else:
        while i!= n:
            if key_value == 26:
                key_value = 1
            else: 
                key_value = key_value + 1 
            i = i + 1 
                    

    for every in alphabet:
        if alphabet.get(every) == key_value:
            return every
