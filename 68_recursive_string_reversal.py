def strin_reversal(string):
    s = len(string)
    if s <= 1:
        return string

    return string[1:] + string[0]

print(strin_reversal('priya'))
    