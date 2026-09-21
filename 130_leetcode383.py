def canConstruct(ransomNote, magazine):
    char_counter = {}
    for i in magazine:
        char_counter[i] = char_counter.get(i, 0) + 1
    for i in ransomNote:
        if char_counter.get(i , 0) <= 0:
            return False
        char_counter[i] -= 1
    return True
    print(char_counter)
print(canConstruct("aa","aab"))