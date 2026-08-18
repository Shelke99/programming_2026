# # Given an integer array nums and an integer k, return the k most frequent elements.
# freq = {}
# nums = [1,2,3,4,5,6]
# for num in nums:
#     freq[num] = freq.get(num,0) + 1
# print(freq)
import heapq
def freq_k(nums,k):
    sz = len(nums)
    freq = {}
    # nums = [num for num in nums]
    # heapq.heapify(nums)
    # print(nums)
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    # print(freq)
    heap = []
    for num,count in freq.items():
        heapq.heappush(heap,(-count, num))
    
    ans = []
    for _ in range(k):
        _,num = heapq.heappop(heap)
        ans .append(num)
    return ans



print(freq_k([1,1,1,2,3,2,3,1,5,4,1,2],2))