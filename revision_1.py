# # Read the positive integer n and  and all of it's divisor and state wether the prime or not ?
# def is_prime(n):
#     divisors = []
   
#     for i in range(1 , n + 1):
#         if n % i == 0:

#             divisors.append(i)
#     if len(divisors) == 2:
#         print(f"{n} is  prime number and its divisor is: {divisors}")
#     else:
#         print(f"{n} is  not prime and  divisors{divisors}")

# is_prime(7)

# # print every number 1 to n  that is divisible by 3 and 5 but not both and show how many such a number and deir sum
# def div_by_3_and_5(n):
#     total_div_sum = 0
#     output = []
#     count = 0
#     for i in range(1, n + 1):
#         # print(i)
#         if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
#             output.append(i)
#             count += 1
#             total_div_sum += i

#     print(f"output : {output}, count : {count}, sum : {total_div_sum}")
# div_by_3_and_5(20)


# # nums is the array and print largest and smallest element together
# #  their position  into an array and the sum ,average and how many element strickly greater then the average
# def array_element(nums):
#     largest_element = float('-inf')
#     smallest_element = float('inf')
#     average = 0
#     total_sum = 0
#     element_above_average = 0
#     for i in range(len(nums)):
#         # largest_element, _i = max(largest_element, nums[i]), i
#         # smallest_element, __i = min(smallest_element, nums[i]), i
#         if nums[i] > largest_element:
#             largest_element, _i = nums[i], i
#         if nums[i] < smallest_element:
#             smallest_element, __i = nums[i],i
#         total_sum += nums[i]
#     average = total_sum / len(nums) 
#     for i in range(len(nums)):
#         if nums[i] > average:
#             element_above_average += 1



#     print(f"max : {largest_element}, index : {_i}, min : {smallest_element}, index : {__i}")
#     print(f"sum_of_all_element : {total_sum}, average : {average}, nums_strickly_greater_than_average : {element_above_average}")
# array_element([4,-1,9,3,2,9])



# # reverse the array in place - without using the second array   
# def swap_array_element(nums):
#     print(f"array element before swapping : {nums}")
#     right = len(nums) - 1
#     left = 0
#     while left <= right:
#         nums[left], nums[right] = nums[right], nums[left]
        
#         left += 1
#     print(f"array element before swapping : {nums}")
# swap_array_element([1,2,3,2,1,5])

an given array nums, define the running sum
def running_sums(nums):
    running_sum = []
    temp = 0
    for i in range(len(nums)):
        temp += nums[i]
        running_sum.append(temp)
    return running_sum
print(running_sums([1,2,3,4]))