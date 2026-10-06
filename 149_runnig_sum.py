def runnigSum(nums):
    runnig_sum = []
    temp = 0
    for i in range(0, len(nums)):
        temp += nums[i]
        runnig_sum. append(temp)
    return runnig_sum
print(runnigSum([1,2,3]))