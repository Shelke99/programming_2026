# class Solution
def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    p = [0] * (n + 1)
    p[0] = 0 
    p[1] = nums[0]
    for i in range(n):
        p[i + 1] = max(p[i], p[i - 1] + nums[i])
    return p[n]
    # p = [0, nums[0]]  # p[0] = 0, p[1] = nums[0]
    
    # for i in range(1, len(nums)):
    #     # p[i] is the last element, p[i-1] is the second to last
    #     next_val = max(p[i], p[i - 1] + nums[i])
    #     p.append(next_val)
        
    # return p[-1]
print(rob([1,2,3,1]))

