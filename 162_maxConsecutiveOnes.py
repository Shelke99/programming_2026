class Solution1:
    def findMaxConsecutiveOnes(self,nums):
        k = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                temp = 0
            else:
                temp += 1
            k = max(k,temp)
            # print(k)
        return k
sol = Solution1()
print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
