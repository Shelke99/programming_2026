from collections import deque
def updateMatrix(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    q = deque()

    dist = [[-1 for _ in range(rows)] for _ in range(cols)]
    # put all 0 in queue
    for r in range(rows):
        for c in range(cols):
            
            if mat[r][c] == 0:
                q.append((r,c))
                dist[r][c] = 0
    # directions
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    while q:
        r,c = q.popleft()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1

                    q.append((nr,nc))
    return dist
print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))