def findMaxAvg(nums, k):
    maxAns = float('inf')
    nsum  = 0
    for i in range(0, k):
        nsum += nums[i]
        maxAns = nsum
    i = 1
    while i < len(nums) - k:
        nsum = nsum - nums[i - 1] + nums[k + i - 1]
        maxAns = max(maxAns,nsum)
        i += 1
    return maxAns / k
print(findMaxAvg([0,1,1,3,3],4))

# print(findMaxAvg([1,12,-5,-6,50,3],4))

