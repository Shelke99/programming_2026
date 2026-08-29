# Basic Operations, Two Ways
# Read two integers and print their sum, difference, and product — 
# (a) computing into a separate result variable, 
# (b) printing the expressions directly without one.
def Basic_op():
    a = int(input("Enter the number first: "))
    b = int(input("Enter the number second: "))

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
    print(f"the value a before he swapping: {a}")
    print(f"the value b before he swapping: {b}")
    # temp = a
    # a = b 
    # b = temp
    a,b = b, a
    print(f"the value a after he swapping: {a}")
    print(f"the value b after he swapping: {b}")
Basic_op()

    