def r_string(string):
    sz = len(string)
    for i in range(sz // 2):
        string[i], string[sz-i-1] =  string[sz-i-1], string[i]
    return string
print(r_string(['h','e','l','o']))
