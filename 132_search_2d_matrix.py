def searchMatrix(matrix, target):
    no_rows =len(matrix)
    no_cols = len(matrix[0])
    lo = 0
    hi = (no_rows * no_cols) - 1
    while (lo <= hi):
        mid = lo + ((hi - lo) // 2)
        r = mid // no_cols
        c = mid % no_cols
        print(matrix[r][c] )
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

        