def rep_substring(a,b):
    S = ''
    sz_a = len(a)
    sz_b = len(b)
    cnt = 0
    while len(S) <= sz_b:
        S += a
        cnt += 1
    if b in S:
        return cnt
    S += a
    cnt += 1
    if b in S:
        return cnt
    return -1
print(rep_substring('abcd', 'cdabcdab'))
