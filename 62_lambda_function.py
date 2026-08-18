# 18.Use a lambda to square elements of a lis
def lambda_func(lst):
    sqr = map(lambda i: i ** 2, lst)
    # sqr = list(map(lambda i: i ** 2, lst))
    return list(sqr)
print(lambda_func([1,2,3,4]))