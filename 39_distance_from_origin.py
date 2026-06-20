# Demonstrate modifying a list within a function. 
def modify_list(lst):
    lst.append(100)
    print("Inside function:", lst)

nums = [1, 2, 3]

print("Before:", nums)

modify_list(nums)

print("After:", nums)