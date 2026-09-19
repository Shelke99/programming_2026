def revision():
    total = 0
    count = 0
    n = int(input("enter the number: "))
    for i in range(1, n+ 1):
        if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
            print(i)
            count += 1
            total += i
    print(f"count of total num is: {count}, sum of num is: {total}")


revision()
