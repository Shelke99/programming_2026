# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?
import heapq
def kth_largest(nums, k):
    sz = len(nums)
    nums = [-num for num in nums]
    heapq.heapify(nums)
    ans = 0
    if sz < k:
        return -1
    for i in range(k):
        ans = -heapq.heappop(nums)
    return ans
print(kth_largest([1,2,3,4,15,17,18,19,14], 4))