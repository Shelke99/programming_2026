19.Use map() to double numbers in a list
def double_num(nums):
    return nums * 2


n = [1,2,3,4,5]
result = map(double_num, n)
    
print(list(result))



print(double_num(5))

# def dnum(nums):

#     dbl = map(lambda a: a * 2, nums)
#     return list(dbl)
# print(dnum([9,8,7,6,5]))