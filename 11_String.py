
# Rule is
# 1. There should be 4 pairs
# 2. It should be unique

def main():
    T =int(raw_input())
    if T != ' ' and T <= 100:
        while T!= 0:
            string = raw_input()
            if !str(string):
                print ' INVALID INPUT'
            elif len(string) <= 1000:
                if len(string)% 4 == 0:                    
                    four = len(string)/4
                    while four != len(string):
                        
                        if string[:four] != string[len(string)-4:]:
                            four = four + 4
                        
                        
                
                
