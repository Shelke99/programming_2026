# 21.Count vowels and consonants in a string.
def vowels():
    string = input('enter the sentance:')
    lst = ['a','e','i','o','u']
    count = 0
    s = len(string)
    for i in range(s):
        if string[i].lower() in lst:
            # print(i)
            count += 1
    return count
print(vowels())

