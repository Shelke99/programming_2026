def matric():
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]

    r = int(input("enter the value: "))
    c = int(input("enter the value: "))
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= 0 and nc >= 0 and nr < 3 and nc < 3:
            print(mat[nr][nc])
matric()
