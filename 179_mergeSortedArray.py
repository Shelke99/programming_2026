class Solution:
    def mergeSortedArray(self,nums1,m,nums2,n):
        i = m - 1
        j = n - 1
        p = (m + n) - 1
        nums1.extend([0] * n)
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
                # p -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        return nums1
sol = Solution()
print(sol.mergeSortedArray([1,2,3],3,[1,2,3],3))