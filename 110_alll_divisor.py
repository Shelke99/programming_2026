def divisor(n):
    divisors = []
    is_prime = 1
    for i in range(1,n + 1):
        if n % i == 0:
            is_prime = 0
            divisors.append(i)
            # n //= i
    if is_prime == 1:
        print("is prime number: ")
    else:
        print("not prime ",n, ":", divisors)
print(divisor(31))
