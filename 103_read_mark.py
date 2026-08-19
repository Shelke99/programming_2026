# Read marks for five subjects and compute the percentage. Print 
# (a) Pass/Fail, (b) a grade from an A–F ladder, and 
# (c) read a grade character and print remarks for it using multi-way selection.

def read_mark():
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
    a = int(input("Enter the number first: "))
    b = int(input("Enter the number second: "))
    op = input("Enter the operator you want do operation(+, −, ×, ÷): ")
    if op in ['+', '−', '×', '÷']:
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '%':
            result = a * b
        else:
            result = "unknown operators and division by zero"
        print(f"the output result is: {result}")
    else:
        print("unknown operators")



read_mark()

