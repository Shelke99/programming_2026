def remove_duplicate(nums):
    left = 0
    for right in range(len(nums)):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
    return left + 1

nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicate(nums)
print(nums[:k])
# print(remove_duplicate(nums))