 
def convert(a,b):
    add = a%b
    if a<=1:
        return str(a)
    else:
        return str(convert(a//b,b)) + str(add)

def find_trail_zero(base):
    found_zero = 0
    count = 0
    for s in base:
        if s == '0':
            found_zero = 1
            count = count + 1
        else:
            if found_zero == 1:
                found_zero = 0
                count = 0

    return count        
    
  

def main():
    P = 1
    array = []
    T =int(raw_input())
    array = raw_input().split()
    
    if len(array) != T:
        print 'Invalid test cases'
    else:
        for a in array:
            if a > 0:
                P = P * int(a)
            else:
                print 'Invalid array values'
        Q = int(raw_input())
        if Q>0 and Q<= 10 ** 5:
            while Q!=0:
                x = int(raw_input())
                if x >= 2 and x <= 10 ** 5:
                	base = convert(P,x)
                	print find_trail_zero(base)
                Q = Q - 1     
        
    


if __name__ == '__main__':
    main() 
