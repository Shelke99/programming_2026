def remove_element(nums,value):
    arr = []
    sz = len(nums)
    k = 0
    for i in range(sz):
        if nums[i] != value:
            nums[k] = nums[i]
            
            k += 1
            # print(nums[k])
    return k

print(remove_element([2,3,3,2], 2))

