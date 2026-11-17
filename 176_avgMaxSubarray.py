class Solution:
    def maxAvgSubarray(self, nums, k):
        nsum = 0
        maxsum = float('-inf')
        for i in range(0, k):
            nsum += nums[i]
            maxsum = nsum
        i = 1
        while i <= len(nums) - k:
            nsum = nsum - nums[i - 1] + nums[k + i - 1]
            maxsum = max(maxsum, nsum)
            i += 1
        return maxsum / k
sol = Solution()
print(sol.maxAvgSubarray([1,12,-5,-6,50,3], 4)) 
