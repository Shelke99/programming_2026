def squareOfArray(nums):
    ans = [0] * len(nums)
    l = 0
    h = len(nums) - 1
    w = len(nums) - 1
    for i in range(0, len(nums)):
        nums[i] = nums[i] * nums[i]
    while l <= h:
        if nums[l] <= nums[h]:
            ans[w] = nums[h]
            h -= 1
        else:
            ans[w] = nums[l]
            l += 1
        w -= 1
    return ans
print(squareOfArray([-2,-1,0,1,2,3,4]))