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

    a = float(input("Enter positive lengths a: "))
    b = float(input("Enter positive lengths b: "))
    c = float(input("Enter positive lengths c: "))

    triangle = a + b + c
    if (a > 0 and b > 0 and c > 0):
        #  triangle inequality
        if (a + b > c) and (a + c > b) and (b + c > a):

            if a == b == c:
                result = "Equilateral"
            elif a == b or b == c or a == c:
                result = "Isosceles"
            else:
                result = "Scalene"
            print(f"Result: {result}")
        else:
            print("Error: The given lengths do not form a valid triangle (triangle inequality failed).")
    else:
        print("side value is must be positive  number")




    




read_mark()

