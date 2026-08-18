def find_target_position(nums, t):
    left = 0
    right = len(nums) - 1

    for i in range(len(nums)):
        mid = (left + right) // 2
        if t == nums[mid]:
            return mid
        elif t > nums[left]:
            left += 1
        else:
            right -= 1
    return left



print(find_target_position([1,2,3,5,6], 4))