# def hello_world():

    # print("Hello World")
    # print(42)
    # print(6 * 7)


    	# Echo an Integer
# Read an integer from the user and print it back.
    # num = int(input('enter the integer value: '))
    # print(f' the given num is: {num}')
# Echo Two Valuesi
# Read two integers and display both with clear labels (e.g. "first = 3, second = 8").
    # num = int(input('enter the first value: ')) 
    # num2 = int(input('enter the second value: '))
    # print(f'the first num is {num}, second = {num2}')  
    # Characters In & Out
# Assign a character constant to a variable and print it; then read a character from the user and print that too.
    # initial = "A"
    # print(f"Assigned character: {initial}")
    # user_input = input("enter the dharacter: ")
    # user_char = user_input[0] if user_input else ""
    # print(f"user entered : {user_char}")

    
    # Read the text "Hello World" from input and print it. Explore why reading word-by-word (token input) drops everything after the space, and how line-based reading fixes it.
    # text = input('enter the text: ')
    # print(text)
    # tokens = input('enter the input:').split()
    # print(tokens[0])


    # Read two integers and print their sum, difference, and product — (a) computing into a separate result variable, (b) printing the expressions directly without one.
    # a = int(input())
    # b = int(input())
    # s = a + b 
    # d = a - b 
    # p = a * b 
    # print(s,d,p)

    # Read two numbers and swap them: (a) using a temporary third variable, (b) without one (arithmetic or XOR).
    # print(f'the value of a : {a} and the value of b: {b}')
    # temp = a
    # a = b 
    # b = temp
    # a = a + b 
    # b = a - b 
    # a = a - b
    # a = a ^ b 
    # b = a ^ b 
    # a = a ^ b
    # print(f'after the value of a: {a} and the value of b: {b}')
    # Convert temperatures both ways: Celsius to Fahrenheit (F = C × 9/5 + 32) and back. Check what goes wrong if 9/5 is computed with integer division.
    # c = float(input('inter temperature in c:' ))
    # F = (c * 9 / 5) + 32
    # print(f'the todays temperature in Farenheit is :o^{F}')
    # # ----------------------------------------
    # F= float(input('inter temperature in Fahrenheit:' ))

    # c = (F - 32) * 5 / 9

    # print(f'the todays temperature in Celsius is :o^{c}')
# hello_world()



# -----------------------------------------------------------------------
# From user-supplied dimensions, compute the area and perimeter of a circle and a rectangle, and the area of a triangle from its three sides (Heron's formula).

# import math
# def shapes():
    # radious = float(input("enter the radious of circle: "))
    # Area_of_circle = math.pi * (radious ** 2) 
    # print(f"the area of corcle is: {Area_of_circle}")
    # Perimeter  = 2 * math.pi * radious
    # print(f"the Perimeter (Circumference) is {Perimeter}")

    # _________________________________________________________________________
    # # rectangle
    # l = float(input("enter the length of rectangle: "))
    # w = float(input("enter the widthe of rcet: "))
    # area = l * w
    # print(f"the area of rectangle is: {area}")

    # perimeter  = 2 * (l + w)
    # print(f"the Circumference of rectangle is: {perimeter}")
    # --- 3. TRIANGLE (Heron's Formula) ---
    # a = float(input("enter the side a of triangle: "))
    # b = float(input("enter the side a of triangle: "))
    # c = float(input("enter the side a of triangle: "))
    # # ---semi_perimeter if triange is
    # s = (a+b+c) / 2

    # triangle_area = math.sqrt(s * (s - a) * (s - b) * ( s - c))
    # print(f' the area of triangle is: {triangle_area}')
    

    # principal = float(input("Enter the Principal amount(Initial investment): "))
    # rate = float(input("Enter the Annual interest rate (in %) "))
    # year = int(input("Enter the years: "))

    # # -------------Interest per Year------------
    # # calculate how much intereat exactly each year
    # interest_per_y = principal * (rate / 100)
    # print(f"each year the Interest was: { interest_per_y}")

    # # -----------------Total interest-----------------
    # # calculate total simple interest and final amount
    # total_interest = principal * (rate / 100) * year

    # print(f" total simple Interest Earned:${total_interest:.2f}")

    # # ------------------Total Amount-------------
    # total_amt = principal + total_interest
    # print(f"total amount after {year} years: ${total_amt:.2f}")

    # for year in range(1, year + 1):
    #     current_amt = principal + (interest_per_y * year)
    #     print(f"End of Year {year}: ${current_amt:.2f}")
    
    
    # Read x and compute x² and x² + 2x.
    # x = float(input("Enter the number (x): "))
    # y = float(input("Enter the number (y): "))
    # square = x ** 2
    # expression_two = (x ** 2) + 2 * x
    # print(f"x² = {square} ")
    # print(f"x² + 2x = {expression_two}")

    # Polynomial Playground
#     # Read x and y and evaluate: (a) x³ + 3x² + 4x − y³, (b) √(2x² + 4y² + x³ + 10), (c) √(4x² + 8y² + x³ + 5) ÷ 2x².
#     a = x ** 3 + 3 * (x ** 2) + 4 * (x) - (y ** 3)
#     print(f"x³ + 3x² + 4x − y³ is : {a:.2f}")

#     b = math.sqrt(2 * (x ** 2) + 4 * (y ** 2) + (x ** 3) + 10)
#     print(f"√(2x² + 4y² + x³ + 10) is: {b:.2f}")

#     c = math.sqrt(4 *(x ** 2) + 8 *(y ** 2) + (x ** 3) + 5) / 2 * (x ** 2)
#     print(f"√(4x² + 8y² + x³ + 5) ÷ 2x² is: {c:.2f}")

    
# shapes()

# Find the roots of ax² + bx + c = 0 from coefficients a, b, c. Use the discriminant to distinguish two real roots, a repeated root, and complex roots — and don't forget a = 0.
# (\(D = b^2 - 4ac\)) // 2a
# import math 
# def q_equation():
#     a = float(input("Enter coefficient a: "))
#     b = float(input("Enter coefficient b: "))
#     c = float(input("Enter coefficient c: "))
#     if a == 0:
#         if b != 0:
#             root = -c / b
#             print(f"Not a quadratic equation (a=0). It is a linear equation with one root: x = {root:.2f}")
#         else:
#             if c == 0:
#                 print("Infinite solutions (0 = 0).")
#             else:
#                 print("No solution (Invalid equation).")
#     else:

#         D = (b ** 2) - (4 * a * c)
#         print(f"\nDiscriminant (D) = {D:.2f}") 
#         if D > 0:
#             root1 = (-b + math.sqrt((D) / 2 * a))
#             root2 = (-b - math.sqrt((D) / 2 * 2))
#             print(f"Two distinct real roots: x1 = {root1:.2f} and x2 = {root2:.2f}")
#         elif D == 0:
#             root = - b / (2 * a)
#             print(f"One repeated real root: x = {root:.2f}")

#         else:
#             real_part = -b / ( 2 * a)
#             imaginary_part = math.sqrt((-D) / (2 * a))  
#             print(f"Two complex roots:")
#             print(f"x1 = {real_part:.2f} + {imaginary_part:.2f}i")
#             print(f"x2 = {real_part:.2f} - {imaginary_part:.2f}i")
# q_equation()
# import math
# def pi_():
    
#     radious = float(input("enter the radious of circle: "))
#     Area_of_circle = math.pi * (radious ** 2) 
#     print(f"the area of corcle is: {Area_of_circle}")
#     Perimeter  = 2 * math.pi * radious
#     print(f"the Perimeter (Circumference) is {Perimeter}")

#     Diameter = 2 * radious
#     print(f"the Diameter of circle is: {Diameter}")
#     pi = Perimeter / Diameter

#     print(f"the value of pii is: {pi}")
# pi_()
# See what your language does when non-numeric text is entered where a number is expected. Then handle it: detect the bad input and re-prompt until a valid number arrives.
# def correct_v():
#     while True:
#         user_val = input("Enter the value: ")

#         try:
#             number = float(user_val)
#             break

#         except ValueError:
#             print(f"❌ '{user_input}' is not a valid number. Please try again.\n")
#         print(f"✅ Success! You entered the number: {number}")
# correct_v()
        
# Read an integer and report whether it is positive, negative, or zero. Then rewrite it as a single (nested) conditional expression.
def condition():
    # read = int(input("enter the number: "))
    # if read > 0:
    #     print(f" it is positive: {read}")
    # elif read < 0:
    #     print(f" number is negative: {read}")
    # else:
    #     print(f"num is zero: {read}")

    # if read > 0:
    #     result = "positive"
    # elif read < 0:
    #     result = "Negative"
    # else:
    #     result = "Zero"
    # print(f"The number is: {result}")

    # result = "positive" if read > 0 else ("negative" if read < 0 else "zero")
    # Read two integers; report if they are equal, otherwise which is larger. Also solve it with a one-line conditional expression.
    a = int(input("enter the value of a: "))
    b = int(input("enter the value of b: "))
    c = int(input("enter the value of c: "))
    # result  = "equal" if a == b else ( "a grater" if a > b else "b greater")
    result = "a is greater" if a > b and a > c else ( "b is greater" if b > a and b > c else "c is greater")


    print(f"The number is: {result}")

condition()





    



    
