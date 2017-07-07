#Write a program that, given a DNA strand, returns its RNA complement (per RNA transcription).
#Both DNA and RNA strands are a sequence of nucleotides.
#The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
#The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
#Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
#G -> C
#C -> G
#T -> A
#A -> U


def DNA_TO_RNA(strand):
    DNA = [ 'G', 'C', 'T', 'A']
    DNA_TO_RNA = [ ['G','C'], ['C','G'], ['T','A'], ['A','U']]
    strand_list = list(strand)
    return_string = ''
    valid = 0
    
    for s in strand_list:
        if s in DNA:
            valid = 1
        else:
            valid = 0
            break

    if valid == 1:
        for s in strand_list:
            for D in DNA_TO_RNA:
                if D[0] == s:
                    return_string = return_string + D[1]

    else:
        return_string = 'Invalid DNA strand'

    return return_string
