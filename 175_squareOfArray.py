class Solution:
    def squareOfArray(self, nums):
        l = 0
        h = len(nums) - 1
        w = len(nums) - 1
        ans = [0] * len(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        while l <=  h:
            if nums[l] > nums[h]:
                ans[w] = nums[l]
                l += 1
                w -= 1
            else:
                ans[w] = nums[h]
                h -= 1
                w -= 1
        return ans
sol = Solution()
print(sol.squareOfArray([-1,0,2,3,4]))