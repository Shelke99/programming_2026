class Solution:
    def findDisappearedNumInArray(self,nums):
        n = len(nums)
        result = []
        for i in range(n):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = - nums[val]
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)
        return result
sol = Solution()
print(sol.findDisappearedNumInArray([4,3,2,7,8,2,3,1]))
