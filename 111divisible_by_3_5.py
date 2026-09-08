def divisible_3_5(n):
    ans = []
    count = 0
    sum_ = 0
    for i in range(1, n + 1):
        if (i % 3 == 0 or i % 5 == 0) and  not (i % 3 == 0 and i % 5 == 0):
            ans.append(i)
            count += 1
            sum_ += i 
    print(ans, count, sum_)
divisible_3_5(20)