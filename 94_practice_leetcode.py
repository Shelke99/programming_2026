def square_element(nums):
    l = 0
    r = len(nums) - 1
    ptr = r 
    ans = [0] * (r +1) 
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            ans[ptr] = nums[l] * nums[l]
            ptr -= 1
            l += 1
        else:
            ans[ptr] = nums[r] * nums[r]
            ptr -= 1
            r -= 1
    return ans
print(square_element([-4,3,5,10]))