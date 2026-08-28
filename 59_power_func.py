# Function to calculate power of a number
# 2. Reuse this function to print powers of 2, 3, -3 for exponents 0–9.
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
def print_powers(base, max_exp):
    for exp in range(max_exp):
        print(f"{base}^{exp} :", power(base, exp))

print_powers(3, 9)
# print_powers(-3, 9)