# Read marks for five subjects and compute the percentage. Print 
# (a) Pass/Fail, (b) a grade from an A–F ladder, and 
# (c) read a grade character and print remarks for it using multi-way selection.

# def read_mark():
#     a = float(input("Entert the mark for subject 1: "))
#     b = float(input("Entert the mark for subject 2: "))
#     c= float(input("Entert the mark for subject 3: "))
#     d = float(input("Entert the mark for subject 4: "))
#     e = float(input("Entert the mark for subject 5: "))

#     total = a + b + c + d + e 
#     percentage = (total / 500) * 100
#     print(f"Total percentage {percentage:.2f}%")

#     if percentage >= 40:
#         status = "Pass"
#     else:
#         status = "Fail"
       

#     if percentage >= 90:
#         grade = "A"
#     elif percentage >= 80:
#         grade = "B"
#     elif percentage >= 70:
#         grade = "C"
#     elif percentage >= 60:
#         grade = "D"
#     elif percentage >= 50:
#         grade = "E"
#     else:
#         grade = "F"

# # (c) read a grade character and print remarks for it using multi-way selection.
#     gread = input("Enter the greag: ").upper()
#     if grade == "A":
#         remark = "Excellent performance"
#     elif grade == "B":
#         remark = "Very good job"
#     elif grade == "C":
#         remark = "Good effort, keep imporving"
#     elif grade == "D":
#         remark = "Satisfactory, but needs more work."
#     elif grade == "E":
#         read = "Just passed, requires attention."
#     elif grade == "F":
#         remark = "Failed. Serious improvement needed."
#     else:
#         remark = remark = "Invalid grade character entered."
#     print(f"REMARK {remark}")



# Read three positive lengths; check the triangle inequality 
# (each pair of sides must sum past the third),
#  then classify: equilateral, isosceles, or scalene.

    # a = float(input("Enter positive lengths a: "))
    # b = float(input("Enter positive lengths b: "))
    # c = float(input("Enter positive lengths c: "))

    # triangle = a + b + c
    # if (a > 0 and b > 0 and c > 0):
    #     #  triangle inequality
    #     if (a + b > c) and (a + c > b) and (b + c > a):

    #         if a == b == c:
    #             result = "Equilateral"
    #         elif a == b or b == c or a == c:
    #             result = "Isosceles"
    #         else:
    #             result = "Scalene"
    #         print(f"Result: {result}")
    #     else:
    #         print("Error: The given lengths do not form a valid triangle (triangle inequality failed).")
    # else:
    #     print("side value is must be positive  number")




    # Read a month number 1–12 and print the month's name and its number of days — 
    # February needs the year to handle leaps.    
    # num = int(input("Enter the number(1-12): "))
    # year = int(input("enter the year: "))
    # # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        
    # if num == 1:
    #     month = "Jan and num 0f days 31"
    # elif num == 2:
    #     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    #         month = "Feb and num of day 29"
    #     else:
    #         month = "Feb and num of day 28"
        
    
        
    # elif num == 3:
    #     month = "Mar and num 0f days 31"
    # elif num == 4:
    #     month = "Apr and num 0f days 31"
    # elif num == 5:
    #     month = "May and num 0f days 31"
    # elif num == 6:
    #     month = "Jun and num 0f days 31"
    # elif num == 7:
    #     month = "Jul and num 0f days 31"
    # elif num == 8:
    #     month = "Aug and num 0f days 31"
    # elif num == 9:
    #     month = "Sep and num 0f days 31"
    # elif num == 10:
    #     month = "Oct and num 0f days 31"
    # elif num == 11:
    #     month = "Nov and num 0f days 31"
    # elif num == 12:
    #     month = "Dec and num 0f days 31"
    # else:
    #     month = "not a month"
    # print(f"Month's and day is {month}")




    # Read three numbers and print them in 
    # ascending order using only comparisons and swaps — no arrays, no library sort.
    # a = int(input("Enter the num1: "))
    # b = int(input("Enter the num2: "))
    # c = int(input("Enter the num3: "))
    # if a > b:
    #     a, b = b, a
    # if b > c:
    #     b, c = c, b
    # if a > b:
    #     a, b = b,a 
    # print(f"Ascending order {a}, {b}, {c}")




    # Compute an electricity bill with slab pricing: the first 100 units at one rate,
    #  the next 100 at a higher rate, everything beyond at a third. Print an itemized bill.

    

    # Read an operator (+, −, ×, ÷) and two numbers, 
    # and apply it. Reject unknown operators and division by zero with clear messages.
#     a = int(input("Enter the number first: "))
#     b = int(input("Enter the number second: "))
#     op = input("Enter the operator you want do operation(+, −, ×, ÷): ")
#     if op in ['+', '−', '×', '÷']:
#         if op == '+':
#             result = a + b
#         elif op == '-':
#             result = a - b
#         elif op == '*':
#             result = a * b
#         elif op == '%':
#             result = a * b
#         else:
#             result = "unknown operators and division by zero"
#         print(f"the output result is: {result}")
#     else:
#         print("unknown operators")



# read_mark()

# # LOOPINGG
# Read n and print the numbers 1 through n.
# Section drill (from the source sheet): 
# solve every problem in this section twice — once with a while loop, once with a for loop

# def looping():
    # n = int(input("Enter the number: "))
    # for i in range(n + 1):
    #     print(f" the given range is: {i}")

    # Print all even numbers from 1 to n by stepping two at a time — no skipping logic needed.
    # for i in range(2,n + 1,2):
    #     print(i)

    # Print 1 to N but skip, in turn: (a) odd numbers, (b) multiples of 3, (c) numbers ending in 5. 
    # Use the loop's skip/continue mechanism rather than restructuring the loop.
    # for i in range(n + 1):
    #     if i % 2 != 0:
    #         continue
    #     if i % 3 == 0:
    #         continue
    #     if i % 10 == 5:
    #         continue
    #     print(i)
    # Read n and compute, in separate loops: the sum 1..n, the sum of the 
    # odd numbers up to n, and the sum of squares 1² + 2² + … + n².
    # sum_all = 0
    # for i in range(1, n+1):
    #     sum_all += i
    # print(f"the sum of  all number is {n}: {sum_all}")



    # odd_all = 0
    # for i in range(1, n + 1):
    #     if i % 2 != 0:
    #         odd_all += i
    # print(f"the sum of odd number is {n}: {odd_all}")


    # sqr_all = 0
    # for i in range(n + 1):
    #     sqr_all += i * i
    # print(f"the sum of square of number is {n}: {sqr_all}")
    

    # Print the multiplication table of a given number (e.g. 7 × 1 through 7 × 10).
    # n = 7
    # i = 1
    # while i < 11:
    #     print(f"{n} x {i} : {i * n}")
    #     i += 1

    # Print the letters A–Z alongside their numeric character codes, one pair per line.
    # for code in range(65,91):
    #     character = chr(code)
    #     print(f"Letters : {character} -> {code}")

    # Compute xʸ for a non-negative integer y using repeated multiplication — no library power function.
    
    # x = float(input("Enter the base (x): "))
    # y = int(input("Enter a non-negative integer exponent (y): "))
    # result = 1.0
    # for i in range(y):
    #     result *= x
    # print(f"{x} raised to the power of {y} is: {result}")
    # #  Read n, then read n numbers one at a time and report their minimum, maximum, and average without storing them all.
    
    # n = int(input("Enter how many numbers you have: "))
        # min_ = None
        # max_ = None
        # sum_ = 0
        # for i in range(1, n + 1):
        #     num = int(input(f"Enter the numbers{i}:  "))
        #     sum_ += num
        #     if min_ is None:
        #         min_ = num
        #         max_ = num
        #     else:
        #         if num < min_:
        #             min_ = num
        #         if num > max_:
        #             max_ = num
        # if n > 0:
        #     average = sum_ / n
        #     print(f"Minimum: {min_}")
        #     print(f"Maximum: {max_}")
        #     print(f"Average: {average:.2f}")


        




    #     nums = [ ]
    #     for i in range(1, n + 1):
    #         nums.append(i)
    #     print(nums)
        
    #     print(min(nums))
    #     print(max(nums))
        
    #     print(sum(nums) / n)



    # Compute 1 + 1/2 + 1/3 + … + 1/n. Watch what happens if the division is done with integers.
    # div = 0
    # for i in range(1, n + 1):
    #     div += (1 / i)
    # print(div)


    # Co.mpute 1 + 2 + 4 + … + 2ⁿ. 
    # Print each partial sum and notice how fast it grows — and where your integer type overflows.
    # p_sum = 0
    # for i in range(n + 1):
    #     p_sum += 2 **i
    #     # term = 2 ** i
    #     # p_sum += term
    #     # print(f"For i = {i:2d} | Added: {term:<20d} | Partial Sum: {p_sum}")
    # print(p_sum)




    # Print the first n terms of the Fibonacci series, keeping only the last two values as you go.
    # f1 = 0
    # f2 = 1
    # for i in range(n + 1):
    #     f3 = f1 + f2
    #     f1 = f2
    #     f2 = f3
    #     print(f3)
    # # print the n terms of fibonacci series
    # if n <= 0:
    #     print("Tis not good ha... please enter  the positive integer")
    # elif n == 1:
    #     print("It's only one number")
    # else:
    #     a,b = 0, 1
    #     print(f"First two number of series is: { a,b}")
    #     for i in range(n + 1):
    #         # print(f"The fibonicci series: {b}")
    #         a, b = b , a + b
    #         print(f"The fibonicci series: {a}")


    # # Compute n! with a loop. Find the largest n your integer type can handle before overflowing.
    # factorial = 1
    # for i in range(1, n + 1):
    #     factorial *= i
    #     print(f"{n} factorial is: {factorial}")


# def digit_divisors():
    # Print a number's digits one per line using division and remainder by 10. In what order do they come out?
    # # qutient = 0
    # rem = 0
    # while n > 0:
    #     rem = n % 10
    #     print(rem)
    #     # qutient 
    #     n = n // 10
    #     # print(n)


    # Count how many digits a number has via repeated division by 10. Mind the edge case n = 0.
    # count = 0
    # while n > 0:
    #     temp = n // 10
    #     count += 1
    #     n = n // 10
    # print(count)
    


    # Add up the digits of a number. Extend: repeat until a single digit remains (the digital root).
    # n = int(input("Enter the number"))
    # num = n
    # while n >= 10:
    #     sum_d = 0
    #     while n > 0:
    #         sum_d += n % 10
    #         n = n // 10
    #     n = sum_d
    #     print(f"the intermideat num is: {n}")

    # print(f"the {num} of digital root is: {n}")
    


    # Reverse a number's digits arithmetically (e.g. 1234 → 4321) — no string conversion.
    # reverse = 0
    # num = n
    # while n > 0:
    #     temp = n % 10
    #     reverse = (10 * reverse) + temp 
    #     n = n // 10
    # print(f"the Reverse of {num} is {reverse}")




    # Check whether a number reads the same reversed, reusing the digit-reversal idea.
    # is_palindrome = 0
    # num = str(n)
    # for i in range( len(num) // 2):
    #     l = num[i]
    #     r = num[len(num)- 1 - i]
    #     # print(f"Comparing position {i}: {l} == {r}")
    #     if l == r:
    #         print("True")
    #     else:
    #         print("False")
    #     # if i == (n-1)
    

    # num = n
    # reverse = 0
    # while n > 0:
        
    #     temp = n % 10
    #     reverse = (10 * reverse) + temp
    #     n = n // 10
    # print(f"reverse is {reverse}")
    # if num == reverse:
    #     print(f"the given {num} is a Palindrome")
    # else:
    #     print(f"{num} not palindrome")



    #  Convert a decimal number to binary via repeated division by 2. Extend to any base from 2 to 16.

    
 
    # binary = ""
    # if n == 0:
    #     binary = "0"
    # while n > 0:
    #     remainder = n % 2
    #     binary = str(remainder) + binary
    #     n = n // 2
    # print(binary)
        


#     # Check whether a number is prime by trial division — and explain why testing divisors up to √n suffices.
# def check_p(n):
#     # n = int(input("Enter the number"))
#     is_prime = 0
#     for i in range(2, n + 1):
#         if n % i == 0:
#             is_prime = 1
#             return True
#             # print("prime")
#         else:
#             return False
                
#         if is_prime == 1:
#             print(f"the given number {n} is prime")
#         else:
#             print("not prime")
# print(check_p(2))



# Find the smallest divisor greater than 1 of a number, stopping the loop 
# as soon as it is found. What does it mean if the answer is the number itself?
# import math
# def find_divisor():
#     n = int(input(f"Enter the number: "))
#     s_div = 0
#     limit = int(math.isqrt(n))
#     for i in range(2, limit + 1):
#         if n % i == 0:
#             s_div = i
#             break
#     print(f" the smallest divisor of {n} is {s_div}")


# Find the smallest divisor greater than 1 of a number, stopping the loop 
# as soon as it is found. What does it mean if the answer is the number itself?
# def find_divisor():
    # n = int(input(f"Enter the number: "))
    # s_div = 0
    # for i in range(2, n + 1):
    #     if n % i == 0:
    #         s_div = i
    #         break
    # # print(f" the smallest divisor of {n} is {s_div}")
    # if s_div == n:
    #     print(f" -> {n} is a Prime Number!")
    # else:
    #     print(f" -> {n} is a Composite Number.")

    # Compute the GCD of two numbers (Euclid's remainder method encouraged) and derive the LCM from it.
    # a = int(input(f"Enter the number: "))
    # b = int(input(f"Enter the number: "))
    # num1 = a 
    # num2 = b 

    # rem = 0
    # while b > 0:
    #     rem = a % b
    #     a = b
    #     print(f"a: {a}")

    #     b = rem
    #     print(f"b: {b}")
    # gcd = a
    # lcm = (num1 * num2) // gcd
    # print("\n--- RESULTS ---")
    # # print(f"Numbers entered : {num1} and {num2}")
    # print(f"Greatest Common Divisor (GCD)   : {gcd}")
    # print(f"Least Common Multiple (LCM)      : {lcm}")




# (a) Find the first number greater than n that is divisible by 7. (b) Find the largest number ≤ N 
# divisible by both 4 and 6.
# Part (b) restated from the sheet — the original "smallest number ≤ N divisible by 4 and 6" is always 12.
    # n = int(input(f"Enter the value of N: "))
    # while True:
    #     num = int(input(f" Enter the number:"))
    #     # if (num > n and num % 7 == 0):
    #     #     print(f"that number {num} is greater than {n} that is divisible by 7. ")
    #     # else:
    #     #     print(f"the enter number: {num} is wrong that not satiesfy the condition number greater than {n} that is  not divisible by 7. ")
    #     # break
    #     # -----------------------------------------b
    #     if num <= n:
    #         if (num % 4 == 0 and num % 6 == 0):
    #             print(f"that number {num} is small or equal than {n} and  is divisible by 4 and 6. ")
    #         else:
    #             print(f"{num} is not divisible by 4 and 6. ")
    #     else:
    #         print(f"that number {num} is not small or not equal t0 {n}")

    #     break

    # # Find all Armstrong numbers in a range — numbers equal to the sum of their digits 
    # # each raised to the digit-count power (e.g. 153 = 1³ + 5³ + 3³).
    # amst = 0
    # num = n
    # while n > 10:
    #     div = []
    #     count = 0
    #     while n > 0:
    #         temp = n % 10
    #         count += 1
    #         div.append(temp)
    #         n = n // 10
    #         # print(div)
    #         # print(count)
    #     for i in div:
    #         amst += i ** count
    #     print(amst)
    #     if num == amst:
    #         print(f"the guven number {num} is Armstrong number {amst}")
    #     else:
    #         print(f"the guven number {num} is Not Armstrong number {amst}")
    # power = len(str(num))
    # while n > 0:
    #     digit = n % 10
    #     amst += digit ** power
    #     n = n // 10
    #     # print(amst)
    # if num == amst:
    #     print(f"The given number {num} is an Armstrong number!")
    # else:
    #     print(f"The given number {num} is NOT an Armstrong number.")


    # # Find all Armstrong numbers in a range — numbers equal to the sum of their digits 
    # # each raised to the digit-count power (e.g. 153 = 1³ + 5³ + 3³).
    # l = int(input("enter the lower range: "))
    # u =  int(input("enter the upper range: "))
    # for num in range(l, u + 1):
    #     digits = str(num)
    #     power = len(digits)

    #     total_sum = sum(int(digit) ** power for digit in digits)

    #     if num == total_sum:
    #         print(num)



    # Check whether a number equals the sum of the factorials of its digits (e.g. 145 = 1! + 4! + 5!).
    # num = int(input("Enter the number: "))
    # n = num
    # sum_ = 0
    # while num > 0:
    #     digits = num % 10
    #     fact= 1
    #     for i in range(1, digits+1):
    #         fact *= i 

    #     num = num // 10
    #     sum_ += fact
    #     print(f"factorial of {digits} is {fact} and the sum is  {sum_}") 
    # if n == sum_:
    #     print(f"the given number is equal to it's factorial sum: {n} = {sum_} ")
    # else:
    #     print(f"the given number is not equal to it's factorial sum: {n} = {sum_} ")
    # sum_ = 0
    
    # while num > 0:
    #     fact = 1
    #     digits = num % 10
    #     for digit in range(1, digits+1):
    #         fact *= digit
    #     num = num // 10
    #     sum_ += fact
    #     print(sum_)



    # Check whether two numbers are amicable: each equals the sum of the other's proper divisors (220 and 284).
    # n1 = int(input("Enter the number 1: "))
    # n2 = int(input("Enter the number 2: "))
    
    # div_sum1 = 0
    # for div in range(1 , n1):
    #     if n1 % div == 0:
    #         div_sum1 += div 

    # div_sum2 = 0   
    # for div in range(1, n2):
    #     if n2 % div == 0:
    #         div_sum2 += div
    # if div_sum1 == n2 and div_sum2 == n1:
    #     print(f"Two numbers are amicable ")
    #     print(f"Divisors of {n1} sum up to {div_sum1}")
    #     print(f"Divisors of {n2} sum up to {div_sum2}")
    # else:
    #      print(f"The numbers {n1} and {n2} are NOT amicable.")




    # For every number from 1 to n, print its prime-factored form (e.g. 12 = 2 × 2 × 3).
    # n = int(input("Enter the number 1: "))
    
    # for num in range(1, n+1):
    #     if num == 1:
    #         print("1 = 1")
    #         continue
        
    #     temp = num 
    #     factor = []
    #     while temp % 2 == 0: #for even numbers
    #        factor.append("2")
    #        temp = temp // 2
        
        
    #     i = 3
    #     while i * i <= temp:
    #         while temp % i == 0:
    #             factor.append(str(i))
    #             temp = temp // i
    #         i += 2


    #     if temp > 2:
    #         factor.append(str(temp))


    #     factor_strt = "x".join(factor)
    #     print(f"{num} = {factor_strt}")


    # Keep reading numbers and summing until the user enters 0, then print the sum 
    # — with a loop that runs at least once. Variant: stop on any negative number instead.
    # total = 0
    # while True:
    #     num = int(input("Enter the number: "))
    #     if num <= 0:
    #         break
    #     total += num
    # print(total)
# find_divisor()






# Ask for a password, allowing up to 3 attempts: print "Access granted" on success or
# "Account locked" after the third failure. Variant: retry forever until correct.
# def pass_auth():
    # pass_key = 0000
    # for attempt in range(1, 4):
    #     num = int(input("Enter the number: "))
    #     if num == pass_key:
    #         print("Access granted")
    #         break
    #     else:
    #         remaining = 3 - attempt
    #         if remaining > 0:
    #             print(f"retry forever until correct.you have only {remaining} attempt")
    # else: 
    #     print("Account locked")


    # Pick a random number 1–100; let the player guess, answering "higher" 
    # or "lower" each time; report the number of attempts on success.

# import random
# def ramdom_guess():
    # guess = random.randint(1, 100)
    # attempt = 0
    # while True:
    #     num = int(input("Enter the Guess number within 1 - 100: "))
    #     attempt += 1
    #     if num == guess:
    #         print("You are the winner")
    #         print(f"It took you {attempt} attempts.")
    #         break
    #     else: 
    #         if num > guess:
    #             print("your guess number is higher")
    #         else:
    #             print("your guess number is lower")
        
            


# ramdom_guess()

# Show a menu of operations (add, subtract, multiply, divide, quit) in a loop; perform the chosen 
# operation each round until the user quits. Builds on Four-Function Calculator.
# def calculator():
#     while True:
#         op = input("Enter the operator (or 'quit'): ").strip().lower()

#         if op == 'quit':
#             print("Goodbye!")
#             break
#         if op not in ['+', '-', '*', '/']:
#             print("Unknon op")


#         a = int(input("Enter the number num1: "))
#         b = int(input("Enter the number num2: "))
        

#         if op in ['+', '−', '×', '÷']:
#             if op == '+':
#                 result = a + b
#             elif op == '-':
#                 result = a - b
#             elif op == '*':
#                 result = a * b
#             elif op == '%':
#                 result = a * b
#                 if b == 0:
#                     result = "unknown operators and division by zero"
#                 else:
#                     result = a / b
#             print(f"the output result is: {result}")
#         else:
#             print("unknown operators")

# calculator()


# Print the multiplication tables 2 through 11 using nested loops
#  — outer loop for the table, inner loop for its entries.
# def table():
#     for i in range(2, 12):
#         # int(input("Enter the number num: "))
#         for j in range(1, 11):
#             print(j * i )
#         print()
# table()

# Print a centered star pyramid of height h, then
#  extend it to a diamond. The trick is counting the spaces before the stars.
# Print the header row to show the numbers 2 through 11
print("    ", end="")
for header in range(2, 12):
    print(f"{header:>5}", end="")
print("\n" + "—" * 55)

# Outer loop: Controls the multiplier entries (1 through 10)
for entry in range(1, 11):
    # Print the side label for the current row
    print(f"{entry:2} |", end="")
    
    # Inner loop: Controls the tables (2 through 11)
    for table in range(2, 12):
        # Calculate the result
        result = table * entry
        # Print the result spaced nicely to align columns
        print(f"{result:>5}", end="")
        
    # Print a new line at the end of each row
    print()



    
    


        
    




