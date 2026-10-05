def remove_element(nums, val):
    k = 0
    for i in range(0, len(nums)-1):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_element([1,2,2,2,3,3], 3))