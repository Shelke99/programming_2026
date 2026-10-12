def optMaxAvg(nums, k):
    global_sum = float('-inf')
    num_sum = 0
    for i in range(k):
        num_sum += nums[i]
        global_sum = num_sum
    i = 1
    while i <= len(nums) - k:
        num_sum = num_sum - nums[i - 1] + nums[k + i - 1]
        
        global_sum = max(global_sum, num_sum)
        
        i += 1
        
    return global_sum / k
print(optMaxAvg([1,12,-5,-6,50,3], 4))