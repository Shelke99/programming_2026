# Count the frequency of each character
char_count = {}

for char in s:
    char_count[char] = char_count.get(char, 0) + 1

# Decrease the count for each character in t
for char in t:
    if char not in char_count:
        return False

    char_count[char] -= 1

    if char_count[char] < 0:
        return False

return True
