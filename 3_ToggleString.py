def ToggleString(char):
    Toggle = ''
    for s in char:
        if s.islower():
            Toggle = Toggle+s.upper()
        elif s.isupper():
            Toggle = Toggle+s.lower()
    print Toggle        
