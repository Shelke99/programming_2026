def positive_integer(n):
    total = 0
    count = 0
    for i in range(1 , n + 1):
        if(i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
            print(f"value : {i}")
            count += 1
            total += i
    print(f"count: {count}, total: {total}")
positive_integer(20)