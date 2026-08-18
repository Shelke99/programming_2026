# 6. Check prime (return 1 or 0), and print all primes up to a given number.
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
        return 1
# print(is_prime(11))

def print_prime(n):
    for i in range(2,n):
        if is_prime(i):
            print(i)
print_prime(11)