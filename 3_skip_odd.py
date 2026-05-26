# 14.Use continue to skip printing odd numbers.
def skip_odd():
    num = [1,2,3,4,5,6,7,8,9,11,12,15]
    ln = len(num)
    for i in range(ln):
        if num[i] % 2 == 1:
            continue
        print(num[i])
skip_odd()