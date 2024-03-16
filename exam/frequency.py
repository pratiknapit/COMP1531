def frequency_get(multilinestr):
    for char in multilinestr:
        if char in ".?!,;:()[]{}-":
            multilinestr = multilinestr.replace(char, "")
    
    line_rem  = multilinestr

    words = line_rem.split()

    dict = {}
    for word in words:
        if word not in dict.keys():
            dict[word] = 1
        else: 
            dict[word] += 1

    freq = ""
    for word in sorted(dict, key=dict.get, reverse=True):
        freq += f"{word.upper()}: {dict[word]}\n"

    freq = freq[:-1]

    return freq

