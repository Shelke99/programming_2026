# 22. Count digit frequency in an integer using loops and list/dictionary.
def digit_frq(n):
    arr = [0] * 10
    while n > 0:
        temp = n % 10
        n = n // 10
        arr[temp] += 1
    print(arr)
digit_frq(5214152)
