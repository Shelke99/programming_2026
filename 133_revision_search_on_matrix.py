def search_matrix(mat,target):
    no_rows = len(mat)
    no_cols = len(mat[0])
    hi = (no_rows * no_cols) - 1
    lo = 0
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        r = mid // no_cols
        c = mid % no_cols
        # print(r)
        print(mid)
        if mat[r][c] == target:
            return True
        elif mat[r][c] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return False
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
        
