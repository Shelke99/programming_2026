# leetcode problem no. 459 is given a string check if it can be constructed by taking a substring of it and appending  multiple copies of the substring together.
def string_construction():
    S = 'abcabcabc'
    # Sb = abc
    
    sz = len(S)
    # print(sz)
    for i in range(sz // 2):
        le = i + 1
        # print(i,le)
        if sz % le != 0:
            continue
        # print(i,le)
            
        rep = sz // le
        print(rep)
        # print(S[le])
        s1 = S[:le]
        print(s1)
        s2 = ''
        for j in range(rep):
            s2 += s1
        if s2 == S:
            return True
    return False

print(string_construction())
