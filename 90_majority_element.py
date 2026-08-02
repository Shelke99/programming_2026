def majority_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key in count:
        if count[key] > len(nums) // 2:
            return key

print(majority_element([2,2,1,1,1,2,2]))