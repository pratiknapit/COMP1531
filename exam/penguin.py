def validate(penguin_number):
    num = penguin_number
    if len(num) != 12:
        return False
    

    if not num[0].isalpha() or num[0].islower():
        return False
    elif not num[1:5].isnumeric():
        return False
    elif not num[5].isalpha() or num[5].islower():
        return False
    elif not num[6:11].isnumeric():
        return False
    elif not num[11].isalpha() or num[11].islower():
        return False
    
    sum = 0
    for n in num[1:5]:
        sum += int(n)

    for n in num[6:11]:
        sum += int(n)

    if sum % 2 != 0:
        return False

    if int(num[10]) % 2 != 0:
        return False

    return True
