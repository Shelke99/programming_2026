def find_substring():
    # leetcode problem no 28
    S = 'The Leo Nardo The Vinchi'
    Sb = 'Nardo'

    sz_s = len(S)
    sz_sb = len(Sb)

    # print(sz_s)
    for i in range(sz_s - sz_sb + 1):
        s1 = S[i:i + sz_sb]
        if s1 == Sb:
            return i
    return -1
    
 

print(find_substring())
