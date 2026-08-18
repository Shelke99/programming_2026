def frequency_map_(n):
    frequency_map = {}

    while n > 0:
        temp = n % 10
        if temp in frequency_map:
            frequency_map[temp] += 1
        else:
            frequency_map[temp] = 1
        n = n // 10
    return frequency_map
print(frequency_map_(123123123455))