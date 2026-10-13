def insert_position(nums, t):
    hi = len(nums)
    lo = 0
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo
print(insert_position([1,3,5,7],2))
