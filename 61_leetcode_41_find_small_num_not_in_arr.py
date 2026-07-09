def find_smallest_num(nums):
    arr = len(nums)
    # # arr.sort()
    # last  = nums[-1]
    # flag = True
    # for i in range(1, last):
        
    #     if i not in nums:
    #         print('i not in arr')
    #         flag = False
    #     return i 
    # if flag == True:
    #     print('is in arr')
    # else:
    #     last += 1
    # return last
    convert_set = set(nums)
    smallest = 1
    while smallest in convert_set:
        smallest += 1
    return smallest
print(find_smallest_num([3,4,5,1]))
