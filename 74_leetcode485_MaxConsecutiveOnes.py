def MaxConsecutiveOnes(nums):
    mx = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            mx = max(mx,count)
        else:
            count = 0
    return mx
print(MaxConsecutiveOnes([1,1,0,1,1,1]))