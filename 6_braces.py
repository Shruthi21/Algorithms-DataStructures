def braces(values):
    dict_brace = { '[':1,'{': 2,'(':3 }
    map_brace = {1: ']', 2:'}', 3: ')'}
    brace_to_compare = ''
    for v in values:
        brace_list = list(v)
        result = []
        for b in brace_list:
            try:
                if dict_brace[b]:
                    brace_to_compare = b

            except KeyError:
                if brace_to_compare != '':
                    try:                         
                        if map_brace[brace_to_compare] == b:
                            continue
                        
                    except KeyError:
                        result.append('NO')
                        break

                   
        result.append('YES')

    return result


if __name__ == '__main__':
    print braces(['{}[]()','{[}]}']) 
