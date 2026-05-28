# pascl's triangle
def triangle(n):
    for i in range(n):
        for j in range(i):
            print('*',end='')
        print()
triangle(10)