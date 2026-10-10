def squareOfSortedArray(nums):
    l = 0
    r = len(nums) - 1
    w = len(nums) - 1
    ans = [0] * len(nums)

    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    while l <= r:
        if nums[l] > nums[r]:
            ans[w] = nums[l]
            l += 1
            w -= 1
        else:
            ans[w] = nums[r]
            r -= 1
            w -= 1
    return ans
print(squareOfSortedArray([-4,-3, 0, 2,10]))