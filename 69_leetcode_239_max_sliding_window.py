from collections import deque
def max_window(nums, k):
    ans = []
    dq = deque()
    for i in range(len(nums)):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)

        while dq and  dq[0] <= i - k:
            dq.popleft()
        dq.append(i)
        if i >= k-1:
            ans.append(nums[dq[0]])
    return ans 
print(max_window([1,3,-1,-3,5,3,6,7], 3))