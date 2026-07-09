# def mutable_(nums):
#     if not isinstance(nums, list) or len(nums) < 2:
#         raise ValueError("inputmust be mutable sequenc")
#     nums[0], nums[1] = nums[1], nums[0]
#     return nums
# print(mutable_([23,43]))

def num_swap(num1, num2):
    num1, num2 = num2, num1
    return num1, num2 
print(num_swap(2,3))