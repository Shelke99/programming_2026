def sliding_max(nums, k):
    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i+k]))
    return result
print(sliding_max([1,3,-1,-3,5], 3))