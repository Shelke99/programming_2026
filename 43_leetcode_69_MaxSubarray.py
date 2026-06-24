def MaxSubArray(nums):
    Max_profit = -1
    sz = len(nums)
    for i in range(sz):

        for j in range(i, sz):
            sum = 0
            for k in range(i, j):
                sum += nums[k]
            Max_profit = max(sum,Max_profit)
    return Max_profit
print(MaxSubArray([5,4,-1,2]))