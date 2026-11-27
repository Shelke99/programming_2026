class Solution:
    def searchInsertPosition(self,nums,t):
        l = 0
        h = len(nums) 
        while l < h:
            mid = l + (h - l) // 2
            if nums[mid] < t:
                l = mid + 1
            else:
                h = mid
        return l
sol = Solution()
print(sol.searchInsertPosition([1,3,5,6],2))