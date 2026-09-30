def reverse_string(s):
    z = len(s)
    i = 0
    j = z - 1
    while i <= j:
        s[i], s[j] = s[j],s[i]
        # print(s)
        return s 
print(reverse_string(['e','a','t']))