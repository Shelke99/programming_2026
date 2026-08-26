def pyramid(n):
    for i in range(n):
        space = n - i -1
        star = i * 2 + 1
        print(" " * space + "*" * star)
    for i in range(n - 2, -1, -1):
        space = n - i - 1
        star = i * 2 + 1
        print(" " * space + "*" * star)



pyramid(5)