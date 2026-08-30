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
    num = int(input("enter the number: "))
    result = "positive" if num > 0 else ("negative" if num < 0 else "zero")
    print(result)
Basic_op()

    