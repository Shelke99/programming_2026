def findMaxAverage(nums: list[int], k: int) -> float:
    global_sum = float('-inf')
    for i in range(0, len(nums) - k + 1):
        sum_ = 0
        for j in range(i, i + k):
            sum_ += nums[j]
        global_sum = max(global_sum, sum_)
    return global_sum / k
print(findMaxAverage([1,12,-5,-6,50,3],4))
print(findMaxAverage([5],1))