import numpy as np 

def monotonic(lists):

    for seq in lists:
        l = list(seq)
        for flt in l:
            if abs(flt) >= 100000:
                return ValueError
        
    out = []
    for seq in lists:
        l = list(seq)

        i = 0
        count_in = 0
        count_de = 0
        while i < len(l)-1:
            if(l[i] <= l[i+1]):
                count_in += 1
            
            if(l[i] >= l[i+1]):
                count_de += 1

            i += 1

        if count_in == (len(l) - 1):
            out.append("monotonically increasing")
            continue

        if count_de == (len(l) - 1):
            out.append("monotonically decreasing")
            continue

        else:
            out.append("neither")
            continue

    return out




