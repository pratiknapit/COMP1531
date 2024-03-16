import functools

def filter_string(inp):

    contains_digit = False

    for character in inp:
        if character.isdigit():
            contains_digit = True

    if contains_digit == True:
        raise ValueError

    no_punt = ""

    for c in inp:
        if c not in ".,\"\';?!":
            no_punt = no_punt + c 
            
    low = no_punt.lower()

    first_upper = ""
    i = 0
    for c in low:
        if i == 0:
            first_upper = low[0].upper()
        else:
            first_upper = first_upper + c
        i += 1

    return first_upper

