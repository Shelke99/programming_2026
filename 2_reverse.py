def reverse(num):
    #123---321
    ans = 0
    while num > 0:
        temp = 0
        temp = num % 10
        ans = (ans * 10) + temp
        num = num // 10
    print(ans)
reverse(91)
