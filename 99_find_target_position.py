def find_target_position(nums, t):
    for i in range(len(nums)):
        if nums[i] >= t:
            return i 
        return len(nums)
print(find_target_position([1,3,4,5],6))