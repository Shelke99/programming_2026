# Read the positive integer n and  and all of it's divisor and state wether the prime or not ?
def is_prime(n):
    divisors = []
   
    for i in range(1 , n + 1):
        if n % i == 0:

            divisors.append(i)
    if len(divisors) == 2:
        print(f"{n} is  prime number and its divisor is: {divisors}")
    else:
        print(f"{n} is  not prime and  divisors{divisors}")

is_prime(7)