# Print formatted patterns: pyramid, diamond, Pascal's triangle.
# pyramid#
def pattern(n):
    space = 6
    star = 1
    for i in range(n):
        
        print(" " * space, '*' * star)
        space -= 1
        star += 2
    for i in range(n):
        print(" " * space, '*' * star)
        space += 1
        star -= 2

pattern(6)