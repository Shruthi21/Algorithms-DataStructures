    I = 0
    result = []
    while I < 100:
        I = int(raw_input())
        result.append(I)

    for r in result:
        if r != 42:
            print r
        else:
            break
