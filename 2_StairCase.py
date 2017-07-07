def staircase(stairs_count=0,symbol='#',default_value=1):
    n = stairs_count
    while stairs_count >= default_value:
        
        print(symbol * default_value + ' ' * (n-1))
        default_value = default_value+1
        n = n-1




if __name__ == '__main__':
    staircase(int(raw_input()))
        
