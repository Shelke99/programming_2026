from collections import deque
def orange_rotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r,c))
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    time = 0
    while q:
        size = len(q)
        while size > 0:
            r,c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            size -= 1
        if q:
           time += 1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1
    return time
print(orange_rotting([[2,1,1],[1,1,1],[0,0,1]]))
