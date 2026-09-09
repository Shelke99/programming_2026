def running_sum(nums):
    r_sum = []
    temp = 0
    for num in range(len(nums)):
        temp += nums[num]
        r_sum.append(temp)
    return r_sum
print(running_sum([1,2,3,4]))