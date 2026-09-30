def reverse(s):
    sz = len(s)
    n = len(s) - 1
    for i in range(0, sz // 2):
        s[i],s[n - i - 1] = s[n - i - 1], s[i]
    return s 
print(reverse(['a','p','p','l','e']))