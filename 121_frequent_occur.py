def frequent_occur():
    arr = []
    freq = {}
    distinct = 0
    most_frequent = float('-inf')
    n = int(input("enter the n: "))
    for i in range(n):
        a = int(input(f"enter the element of: {i} "))
        arr.append(a)
        # print(arr)
    for j in arr:
        if j in freq:
            freq[j] = freq[j] + 1
        else:
            freq[j] = 1
    # print(freq)
    
    for key, value in freq.items():
        # print(key, value)
        if most_frequent < value:
            most_frequent = key

        if value >= 1:
            distinct += 1

    print(f"distinct: {distinct}, most_frequent: {most_frequent}")






frequent_occur()
