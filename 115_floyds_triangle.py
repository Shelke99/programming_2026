# Floyd's Trianglei
# Print Floyd's triangle: consecutive numbers 1 / 2 3 / 4 5 6 / 
# … in rows. Variant: each row repeats its row number instead.
def floyd_triangel(n):
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i):
            print(count, end="")
            count += 1
        print()
floyd_triangel(4)
