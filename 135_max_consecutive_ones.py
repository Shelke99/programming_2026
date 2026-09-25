def maxConsecutiveOnes(nums):
    max_count = 0
    cur = 0
    for l in range(len(nums)):
        if nums[l] == 1:
            cur += 1
            max_count = max(max_count, cur)
        elif nums[l] == 0:
            cur = 0
    

        
    return max_count
print(maxConsecutiveOnes([1,1,0,1,1,1,1,0,0,0]))
