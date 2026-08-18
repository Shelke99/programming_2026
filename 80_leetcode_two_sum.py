def two_sum(source,target):
    s = len(source)
    seen = {}
    for i, num in enumerate(source):
        is_in = target - num
        if is_in in seen:
            return [seen[is_in], i]
        seen[num] = i 
print(two_sum([2,7,11,15],9))