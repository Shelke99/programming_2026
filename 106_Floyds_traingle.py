# Print Floyd's triangle: consecutive numbers 1 / 2 3 / 4 5 6 /
#  … in rows. Variant: each row repeats its row number instead.
def floyd_triangle():
    # # for i in (n + 1):
    # i = 1
    # while i <= n:
    #     for j in range(i):
    #         print(i, end= " ")
    #     print()
    #     i += 1

    rows = int(input("enter the num: ")) 
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end= ' ')
            num += 1
        print()
        
floyd_triangle()