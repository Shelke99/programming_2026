def single_element(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key in count:
        if count[key] == 1:
            return key

print(single_element(nums = [4,1,2,1,2]))