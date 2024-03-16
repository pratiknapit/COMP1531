def acronym_make(inputs):

    list = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    acronyms = []
    
    for strings in inputs: 

        acro = "" 

        split_string = strings.split()

        for word in split_string:
            c = word[0]
            if c not in list:
                l = c.upper()
                acro = acro + l

        acronyms.append(acro)

    return acronyms



    
