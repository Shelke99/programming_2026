# 17. Print multiplication tables for 1 to 10.
def table():
    for i in range(1,11):
        for j in range(1,11):
            print('the table of ',i,'=',i * j)
        print()

table()