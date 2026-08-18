# 16.Find the smallest divisor of a number greater than 1 using break.
def divisor():
    num = 20
    divis = 0
    for i in range(2, num):
        if num % i ==0:
            divis = i
            break
    print(divis)
divisor()