def UtopiaTree(cycle):

    resultHieght = []
    for x in cycle:
        Height = 1
        spring = 1
        summer = 0

        while x != 0:
            if spring == 1:
                spring = 0
                summer = 1
                Height = Height * 2
            elif summer == 1:
                summer = 0
                spring = 1
                Height+= 1

            x-= 1
        resultHieght.append(Height)
    return resultHieght        
        
        


if __name__ == '__main__':
    t = int(raw_input().strip())
    cycle = []
    for a0 in xrange(t):
        n = int(raw_input().strip())
        cycle.append(n)
    
    for h in UtopiaTree(cycle):
        print h
     
