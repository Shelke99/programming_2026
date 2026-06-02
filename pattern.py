# square
def square(n):
    # for i in range(n):
    #     for j in range(n):
    #         print("*",end='')
    #     print()
    #######piryamid#########
    # for i in range(1,n):
    #     print("*" * i)

    # for i in range(5, 0,-1):
    #     print("*" * i)      
    # n = int(input('enter the num:'))
    # for i in range(n):
    #     print("*" * i)
    # for i in range(n):
    #     print("*")
    space = 3
    star = 1
    for i in range(1,n):
       print(" " * space, "*" * star) 
       space -= 1
       star += 2            


square(5)