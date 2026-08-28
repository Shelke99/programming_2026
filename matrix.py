def mat():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    row = len(mat)
    # col = 3

    # trans = []
    for r in range(row):
        for c in range(r,row):
            mat[r][c],mat[c][r] = mat[c][r],mat[r][c]
    print(mat,end='')
mat()