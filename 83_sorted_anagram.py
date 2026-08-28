def anagram(s,t):
    if sorted(s) == sorted(t):
        return True
print(anagram('anagram', 'nagaram'))