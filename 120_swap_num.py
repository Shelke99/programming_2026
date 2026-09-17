def divisible_reminder(a,b):
    count = 0
    total = 0
    store = []
    big = float('-inf')
    if (a > b):
        a, b = b, a 
    for i in range(a, b + 1):
        
        if (i % 4 == 1 and i % 6 == 1) and not (i % 5 == 0):
            print(i)
            count += 1
            total += i
            store.append(i)
    print(count, total, store)
    for j in range(len(store)):
        
        if big < store[j]:
            big = store[j]
    print(big)



divisible_reminder(50, 1)