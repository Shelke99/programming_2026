# .Find the smallest divisor of a number greater than 1 using break.
def divisor(n):
    for i in range(2,n):
        if n % i == 0:
            print('is smallest divisor:',i)
            break
divisor(18)