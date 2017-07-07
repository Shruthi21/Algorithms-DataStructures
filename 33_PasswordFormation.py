#!/bin/python

import sys


n = int(raw_input().strip())
vowels = ['a','e','i','o','u']
consonents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
password = ''
password_list=[]
i = 0
is_vowel = 0

for v in vowels:
    for c in consonents:
        password = ''
        while len(password) != n:
            if is_vowel == 0:
                password = password + v
                is_vowel = 1
            else:
                password = password + c
                is_vowel = 0
                
        if password not in password_list:
            password_list.append(password)

is_vowel = 1
for c in consonents:
    for v in vowels:
        password = ''
        while len(password) != n:
            if is_vowel == 1:
                password = password + c
                is_vowel = 0
            else:
                password = password + v
                is_vowel = 1
        if password not in password_list:
            password_list.append(password)                  
                    
for p in password_list:
    print p
    

          
