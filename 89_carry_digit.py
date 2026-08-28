def plusOne(digit):
    for i in range(len(digit)-1,-1,-1):
        if digit[i] < 9:
            digit[i] += 1
            return digit
        
        digit[i] = 0
    return [1] + digit



print(plusOne([1,2,3]))
print(plusOne([1,2,9]))
