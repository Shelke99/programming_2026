# 19. Calculate the average of positive numbers entered (stop on zero). 
def avg():
    count = 0
    total = 0
    ans = 0
    while True:
        n = int(input("enter the number:"))
        if n == 0:
            break
        elif n > 0:
            count += 1
            total += n
        else:
            print("is neative number")
    ans = total // count
    print(ans)
avg()
