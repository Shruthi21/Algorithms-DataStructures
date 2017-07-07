def Polygons(measure):
    square = 0
    rectangle = 0
    polygon = 0
    high = len(measure)
    result = []
    for i in range(0,len(measure)):
        if len(measure[i]) != 4:
            return 'Invalid input'
        else:
            for j in range(0,len(measure[i])):
                if measure[i][j]<0:
                    measure[i][j] = 0
                    exit
        
    
    while high != 0:
        high-=1
        if measure[high][0] == 0 or measure[high][1] == 0 or measure[high][2] == 0 or measure[high][3] == 0:
            polygon+=1
        elif measure[high][0] ==  measure[high][2] and measure[high][1] ==  measure[high][3] and measure[high][1]!=measure[high][2]:
            rectangle+=1
        elif measure[high][0] ==  measure[high][1] and  measure[high][1]== measure[high][2] and measure[high][2] ==  measure[high][3]:
            square+=1
        else:                   
            polygon+=1        
           
    return str(rectangle) + ' '+ str(square) + ' ' +str(polygon)
        

if __name__ == '__main__':
    measure =[]
    line = raw_input()
    
    while line != "":
        A,B,C,D=map(int,line.split())
       
        measure.append([A,B,C,D])
        line=raw_input()

    if measure != []:
        print Polygons(measure)
            
