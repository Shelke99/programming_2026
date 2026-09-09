def swap_element(nums):
    print("before swapping: ",nums)
    l = 0
    r = len(nums) - 1
    while l <=  r:
        nums[l], nums[r] = nums[r], nums[l]
        
        l += 1
        r -= 1
    
    print("after the swapping: ", nums)
        



swap_element([1,2,3,2,1,5])