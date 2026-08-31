# Basic Operations, Two Ways
# Read two integers and print their sum, difference, and product — 
# (a) computing into a separate result variable, 
# (b) printing the expressions directly without one.
import math
def Basic_op():
#     a = int(input("Enter the number first: "))
#     b = int(input("Enter the number second: "))

    # op = input("enter the op etation( + - * ): ")

    # if op == '+':
    #     result = a + b
    # elif op == '-':
    #     result = a - b
    # elif op == '*':
    #     result = a * b
    # else:
    #     result = 'not match any op'
    # # print(f"result: {result}")
    # print(f"sum: {a + b}")
    # print(f"difference: {a - b}")
    # print(f"product: {a * b}")
    

# Swap Two Numbers
# Read two numbers and swap them:
# (a) using a temporary third variable, 
# (b) without one (arithmetic or XOR).
    # print(f"the value a before he swapping: {a}")
    # print(f"the value b before he swapping: {b}")
    # # # temp = a
    # # # a = b 
    # # # b = temp
    # # a,b = b, a

    # # a = a + b
    # # b = a - b 
    # # a = a - 
    # a = a ^ b
    # b = a ^ b 
    # a = a ^ b
    # print(f"the value a after he swapping: {a}")
    # print(f"the value b after he swapping: {b}")


# Convert temperatures both ways: Celsius to Fahrenheit (F = C × 9/5 + 32) and back. 
# Check what goes wrong if 9/5 is computed with integer division.
    # t = float(input("Enter the temperature in celcious: "))
    # f = t * (9 / 5) + 32
    # print("fahrebheit: ",f)
    # c = t * (5 / 9) - 32
    # print(c)

    # Shapes: Area & Perimeteri
    # From user-supplied dimensions, compute the area and perimeter of a circle and 
    # a rectangle, and the area of a triangle from its three sides (Heron's formula).
    # r = int(input("Enter the circle diam: "))
    # area = math.pi * (r ** 2)
    # print(area)
    # perimeter = 2 * math.pi * r
    # print(perimeter)
    # s = []
    # for i in range(3):
    #     ss = int(input(f"Enter the side of ractangle: {i} :"))
    #     s.append(ss)
    # print(s)
    # sp = (s[0] + s[1] + s[2]) / 2
    # print(sp)
    # area = math.sqrt(sp * (sp - s[0]) * (sp - s[1]) * (sp - s[2]))
    # print(f'area of the ractangee is : {area}')
    



    # Simple Interesti
    # Read principal, annual rate, and years; print the simple interest 
    # and the total amount. Then print the amount at the end of each year.
    # p = int(input("Enter the principal amount"))
    # y = int(input("Enter the year: "))
    # r = float(input("Enter the rate of interaste: "))
    # i = ( p * r * y) / 1000
    # t = p + i
    # print(i)
    # print(t)
     



    #   Square & Friendsi
    #  Read x and compute x² and x² + 2x.
    # a = int(input("enter the value of a: "))
    # eqn = x ** 2 +  2 * x

    # Polynomial Playground
    # Read x and y and evaluate: (a) x³ + 3x² + 4x − y³, (b)
    # √(2x² + 4y² + x³ + 10), (c) √(4x² + 8y² + x³ + 5) ÷ 2x².
    # b = int(input("enter the value b: "))
    # a = x ** 3 + x ** 2 + 4 * x - y ** 3
    # print(a)
    # b = math.sqrt(2 * x ** 2 + 4 * y ** 2 + x ** 3+ 10)
    # print(b)
    # c = math.sqrt(4 * x ** 2 + 8 * y ** 2 + x ** 3 + 5) / 2 * x ** 2
    # print(c)

    # Quadratic Rootsi
    # Find the roots of ax² + bx + c = 0 from coefficients a, b, c. Use the discriminant to 
    # distinguish two real roots, a repeated root, and complex roots — and don't forget a = 0.

    # c = int(input("Enter the value of c: "))
    
    # s = b ** 2 - (4 * a * c)
        
    # if s < 0:
    #     print("missing")
    # elif s == 0:
    #     r1 = -b / (2 * a)
    #     print("is real root: ")
    # else:
    #     r = math.sqrt(s)

    #     r1 = - b + (r / 2 * a)
    #     r2 = - b - ( r / 2 * a)
    #     # print(root)
    #     print(f"real root1 : {r1}")
    #     print(f"real root2 : {r2}")

    # Guard the Input
    # See what your language does when non-numeric text is entered where a number is expected. 
    # Then handle it: detect the bad input and re-prompt until a valid number arrives.
    # while True:
    #     in_p = input("enter the input number: ")
    #     try:
    #         num = int(in_p)
    #         print(f"sucessfull your number is: {in_p}")
    #         break
    #     except ValueError:
    # #         print("try again")    
    # 17	Positive, Negative or Zeroi
    # Read an integer and report whether it is 
    # positive, negative, or zero. Then rewrite it as a single (nested) conditional expression.
    # num = int(input("enter the number: "))
    # result = "positive" if num > 0 else ("negative" if num < 0 else "zero")
     

    # # 18	Larger of Twoi
    # Read two integers; report if they are equal, 
    # otherwise which is larger. Also solve it with a one-line conditional expression.
    # num2 = int(input("enter the number: "))
    # if num == num2:
    #     print("repot...they are equal")
    # else:
    #     result = "num is greater" if num > num2 else "num2 is greater" 
    # print(result)
    

    # 19	Largest of Threei
    # Read three integers and find the largest.
     
    # num3 = int(input("enter the number: "))
    # if num == num2 == num3:
    #     result = "repot...they are equal"
    # else:
    #     result = "num is greater" if num > num2 and num > num3 else ("num2 is greater" if num2 > num and num2 > num3 else "num3 is greater") 
    # print(result)

    # Odd or Even
    # ead an integer and report odd or even. Then write it as a one-line conditional expression.
    # if num < 0:
    #     result = "is negative"
    # else:
    #     result = "num is even" if num % 2 == 0 else "num is odd"
    # print(result)



    # Leap Yeari
    # Determine whether a given year is a leap 
    # year using the full rule: divisible by 4, except centuries, unless divisible by 400.

    # digit = input("enter the value: ")
    # result = "is leap" if num % 4 == 0 and num % 100 != 0 or num % 400 == 0 else "not leap year"
    # print(result)
    # 22	Letter, Digit or Symbol?
    # Read a character and classify it as a letter, a digit, or a special character.
    # result = "is number" if num in [0-9] else ("character" if num in isalpha(a-z and A-Z) else "special char")
    
    # if digit.isalpha():
    #     result = "is letter"
    # elif digit.isdigit():
    #     result = "is number"
    # elif digit in [ '#','$','&','*','_','-' ]:
    #     result = "special char"
    # else:
    #     result = "is somthing wrong"
    
    # print(result) 
  
    
    # if digit in ['a-z or A-Z']:
    #     result = "is letter"
    # elif digit in [0-9]:
    #     result = "is number"
    # elif digit in [ '#','$','&','*','_','-' ]:
    #     result = "special char"
    # else:
    #     result = "is somthing wrong"
    
    
    # Vowel, Consonant & Casei
    # Read a letter and report (a) vowel or consonant, (b) uppercase or lowercase.
    # if digit.isdigit():
    #     result = "is u enter the digit"
    # elif digit in ['a','e','i','o','u']:
    #     result = "is Vowel"
    # else:
    #     result = "is Consonant"
    # print(result)


    # Profit or Lossi
    # From cost price and selling price, report profit, loss, or break-even — and the amount.
    # cost = int(input("enter the cost price: "))
    # sell = float(input("enter the selling price: "))
    # if cost > sell:
    #     result = "loss"
    # elif cost < sell:
    #     result = "Profit"
    # elif cost == sell:
    #     result = "break-even"
    # else:
    #     result = "anknon"
    # print(result)



    # Number Range Ladderi
    # Warm-up: compare a number to 10 and print "small" / "large" / "equal". Then the ladder: below 100 
    # "small", 100–200 "large", 201–300 "bigger", 301–400 "largest", above 400 "very large".
    # a = int(input("Enter the number: "))
    # if a > 0:
    #     if 100 <= a <= 200:
    #         result = "large"
    #     elif 200 < a <= 300:
    #         result = "bigger"
    #     elif 300 < a <= 400:
    #         result = "largest"
    #     elif a < 400:
    #         result = "very largest"
    #     else:
    #         result = "enter the correct number"
    #     print(result)
    # else:
    #     print("enter the correct num")

    # Day of the Weeki
    # Read a number 1–7 and print the weekday name. Solve twice: with an if/else
    # ladder and with your language's multi-way selection; compare the readability.

    # i = int(input(f"Enter the number (0-6): "))
        
    # if i == 0:
    #     result = "sunday"
    # elif i == 1:
    #     result = "M"
    # elif i == 2:
    #     result = "T"
    # elif i == 3:
    #     result = "W"
    # elif i == 4:
    #     result = "T"
    # elif i == 5:
    #     result = "F"
    # elif i == 6:
    #     result = "S"
    # else:
    #     result = "not match"
    # print(result)

    # 27	Valid Triangle — Anglesi
    # Read three angles and check whether they form a valid triangle: 
    # every angle greater than 0° and the three summing to exactly 180°.
    # a = int(input("enter the ange 1: "))    
    # b = int(input("enter the ange 2: "))
    # c = int(input("enter the ange 3: "))
    # t = a + b + c 
    # if (a > 0 and b > 0 and c > 0):
    #     if t == 180:
    #         print("Valid Triangle: The angles form a triangle.")
    #     else:
    #         print("Invalid Triangle: The sum of angles is not 180 degrees.")
    # else:
    #     print("Invalid Triangle: Angles must be greater than 0 degrees.")

    #30	Month Lookupi
    # Read a month number 1–12 and print the month's name and its number of days — February needs the year to handle leaps. 
    # m = int(input("Enter the month num (1-12): "))
    # year = int(input("enter the year: "))
    
    # if m == 2:
    #     if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    #         result = "29 and Feb" 
    #     else:
    #         result = "28 and Feb"

    # elif  m in [4,6,9,11]:
    #     if m == 4:
    #         result = "30 and AP"
    #     elif m == 6:
    #         result = "30 and Jun"
    #     elif m == 9:
    #         result = "30 and sep"
    #     else:
    #         result = "30 and nov"
    # elif m in [1,3,5,7,8,10,12]:
    #     if m == 1:
    #         result = "Jan and 31"
    #     elif m == 3:
    #         result = "Mar and 31 days"
    #     elif m == 5:
    #         result = "May and 31 day"
    #     elif m == 7:
    #         result = "Jul and 31 days"
    #     elif m == 8:
    #         result = "Aug and 31 days"
    #     elif m == 10:
    #         result = "Oct and 31 days"
    #     elif m == 12:
    #         result = " Dec and 31 days"
    #     else:
    #         result = "valueError"
    # else:
    #     result = "Not match"
    # print(result)
    


    # Sort Three Numbersi
    # Read three numbers and print them in ascending order using only comparisons and swaps — no arrays, no library sort.
    a = int(input("enter the num 1"))
    b = int(input("enter the num 2: "))
    c = int(input("enter the num 3: "))

    if a > b :
        a , b = b , a
    if b > c:
        b , c = c , b
    if a > b:
        a , b = b , a
    result = a,b,c 
    print(result) 



Basic_op()

    