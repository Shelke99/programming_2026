class Solution:
    def findDisappearedNumInArray(self, nums):
        # sz = 
        seen = set(nums)
        result = []
        for i in range(1, len(nums)):
            if i not in seen:
                result.append(i)
        return result
sol = Solution()
print(sol.findDisappearedNumInArray([4,3,2,7,8,2,3,1]))


