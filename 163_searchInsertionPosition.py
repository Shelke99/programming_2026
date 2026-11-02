class Solutuin:
    def searchInsertPosition(self,nums,k):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < k:
                lo = mid + 1
            else:
                hi = mid 
        return lo
sol = Solutuin()
print(sol.searchInsertPosition([1,2,4,5,6],7))
