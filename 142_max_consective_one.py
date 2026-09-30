def max_ones(nums):
    ans = 0
    temp = 0
    for  i in nums:
        if i != 1:
            temp = 0
        temp += i
        ans = max(ans, temp)
    return ans
print(max_ones([1,0,0,1,1,1,0,0])) 
