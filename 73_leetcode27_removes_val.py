def removes_val(nums, val):
    w = 0
    for read in range(len(nums)):
        if nums[read] == val:
            # nums[read] = '_'
            continue
        
        nums[w] = nums[read]
        w += 1
    return w,nums
print(removes_val([0,1,2,2,4,3,5,2],2))