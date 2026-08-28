def map_k(lst, k):
    sz = len(lst)
    for i in range(sz):
        if lst[i] == k:
            lst[i] = '_'
    return lst
print(map_k([3,2,2,3], 3))