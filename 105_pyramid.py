def pyramid(h):
    for i in range(h):
        space = h -i - 1
        star = 2 * i -1
        print(" " * space + "*" * star)
    for i in range(h - 2, -1, -1):
        space = h - i - 1
        star = 2 * i + 1
        print(" " * space + "*" * star)


pyramid(5)