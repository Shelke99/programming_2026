def validAnagram(s,t):
    if len(s) != len(t):
        return False
    
    
    s_freq ={}
    t_freq = {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    for char in s_freq:
        if char not in t_freq or s_freq[char] != t_freq[char]:
            return False
    return True

print(validAnagram("anagram", "nagaram"))