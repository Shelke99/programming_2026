# Write a function to compute power (base, exponent). 
def power_function():
    base = int(input("enter the base value:"))
    exp = int(input("enter the exp value:"))
    ans = 1
    for i in range(1, exp + 1):
        ans *= base
    return ans
print(power_function())