# find the duplicate number and remove the duplicate and inplace the arrays number i ascending order 
def find_duplicate(nums):
    w = 0
    r = 1
    while r < len(nums):
        if nums[w] != nums[r]:
            w += 1
            nums[w] = nums[r]
            
        r += 1
    print(nums)
    return w + 1

print(find_duplicate([0,0,1,1,1,2,2,3,3,4]))