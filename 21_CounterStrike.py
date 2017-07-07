#https://en.wiktionary.org/wiki/Manhattan_distance
def main():
    t = int(raw_input())
    n_m_d = []
    n = 0
    m = 0
    d = 0
    x_y_1 = []
    x_y_2 = []
    source = []
    target = []
    distance = []
    possible = 0
    manhattan_distance = 0
    counter = 0
    while t != 0:
        t = t - 1
        n_m_d = map(int,raw_input().split())
        
        if len(n_m_d) == 3:
            d = n_m_d[2]
            n = n_m_d[0]
            while n != 0:
                n = n - 1
                x_y_1 = map(int,raw_input().split())
                #print x_y_1
                source.append(x_y_1)
                #print source
            m = n_m_d[1]
            while m != 0:
                m = m - 1
                x_y_2 = map(int,raw_input().split())
                #print x_y_2
                target.append(x_y_2)
                #print target
            manhattan_distance = 0                
            for a,b in zip(source,target):
                manhattan_distance = abs(( a[0] - b[0] )) + abs(( a[1] - b[1] ))
                distance.append(manhattan_distance )

            for dis in distance:
                if dis > d:
                    print 'NO'
                    counter = 0
                    break
                else:
                    counter = counter + 1

                if counter > (n_m_d[1]/2):
                    print 'YES'
                    break           
        
       
    
                
   
if __name__ == '__main__':
    main()  
