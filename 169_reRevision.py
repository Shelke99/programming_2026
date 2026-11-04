class Solution:
    def runningSumOfOneDArray(self,nums):
        ans = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            ans.append(temp)
        return ans
sol = Solution()
print(sol.runningSumOfOneDArray([1,2,3,4]))