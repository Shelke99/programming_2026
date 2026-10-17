def runnig(nums):
    s = len(nums)
    num_sum = 0
    for i in range(s): 
        num_sum += nums[i]
        print(num_sum)
    
    return num_sum
print(runnig([1,2,3,4,5]))