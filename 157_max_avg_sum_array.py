def maxAvg(nums, k):
    glob_sum = float('-inf')
    nsum = 0
    for i in range(0,k):
        nsum += nums[i]
        glob_sum = nsum
    i = 1
    while i <= len(nums) - k:
        nsum = nsum - nums[i - 1] + nums[k + i - 1]
        glob_sum = max(glob_sum,nsum)
        i += 1
    return glob_sum / k
print(maxAvg([1,12,-5,-6,50,3],4))