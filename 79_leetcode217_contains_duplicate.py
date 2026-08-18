def contain_duplicate(lst):
    # s = len(lst)
    seen = set()
    # for i in range(s):
    #     if lst[i] in seen:
    #         return True
    #     seen.add(lst[i])
    # return False

    for l in lst:
        if l in seen:
            return True
        seen.add(l)
    return False
print(contain_duplicate([1,2,3,1]))



    

    