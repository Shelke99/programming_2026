class Solution:
    def removeDuplicate(self,nums):
        k = 1
        i = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
                # i += 1
            else:
                i += 1
        return k
sol = Solution()
print(sol.removeDuplicate([0,1,1,2,3,4,5,5]))

