# 20. Check if a number is a palindrome.
def is_palindrom(n):
    s = str(n)
    j = 0
    k = len(s) - 1
    while j < k:

        if s[j] == s[k]:
            j += 1
            k -= 1
        else:
            return False
            print('the given number is not palindrom:')
    return True
    # return s == s[::-1]

print(is_palindrom(121))
print(is_palindrom(1210))
