#Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
#The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that the resulting alphabet is backwards. The first letter is replaced with the last letter, the second with the second-last, and so on.
#An Atbash cipher for the Latin alphabet would be as follows:
#Plain:  abcdefghijklmnopqrstuvwxyz
#Cipher: zyxwvutsrqponmlkjihgfedcba

Plan_Cipher = { 'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p', 'l':'o', 'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g', 'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a' }
Special_Char = [' ','.',',']
Numbers = '0123456789'

def encode(string):
    
    encode_string = ''
    string_list = list(string.lower())
    
    for s in string_list:
        if s not in Special_Char:
            if s not in Numbers:
                encode_string = encode_string + Plan_Cipher[s]

    return encode_string


def decode(string):
    
    decode_string = ''
    string_list = list(string.lower())
    for s in string_list:
        if s not in Special_Char:
            if s not in Numbers:
                decode_string = decode_string + Plan_Cipher[s]
    return decode_string
