GUESS_NUM = 15
def guess_num(num):
    if num == GUESS_NUM:
        return 0
    elif num > GUESS_NUM:
        return -1
    else:
        return 1

def number_check(n):
    lo = 0
    hi = n 
    while lo <= hi:
        pick = lo + (hi - lo) // 2
        res = guess_num(pick)
        if res == 0:
            return pick
        if res == -1:
            hi = pick - 1
        elif res == 1:
            lo = pick + 1
    return -1

print(number_check(30))


