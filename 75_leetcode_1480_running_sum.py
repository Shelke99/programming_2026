def running_1DArray_sum(nums):
    ans = []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        ans.append(sum)
    return ans
print(running_1DArray_sum([1,2,3,4]))