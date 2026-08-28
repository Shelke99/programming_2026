# 20. Use filter() to keep only even numbers.
def filter_even(nums):

    # only_even = list(map(lambda a: "Even" if a % 2 == 0 else "Odd",nums))
    # return only_even
    
    only_even = list(filter(lambda a: a % 2 == 0, nums))
    return only_even
print(filter_even([1,2,3,4,5,6,7,8,9]))