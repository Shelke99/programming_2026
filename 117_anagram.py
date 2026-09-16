# given two string a and t return true if t is an anagram of s and false o.w 
def anagram(s,t):
    s1 = {}
    s2 = {}
    for ch in s:
        if ch in s1:
            s1[ch] = s1[ch] + 1
        else:
            s1[ch] = 1
    for ch in t:
        if ch in s2:
            s2[ch] = s2[ch] + 1
        else:
            s2[ch] = 1
    for ch in s1:
        if ch not in s2:
            return False

        if s1[ch] != s2[ch]:
            return False

       
    return True
print(anagram('rat', 'car'))
print(anagram('anagram', 'nagaram'))