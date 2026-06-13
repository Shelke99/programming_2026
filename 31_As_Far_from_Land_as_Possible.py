# leetcode1162_As Far from Land as Possible
from collections import deque
def water_from_land(grid):
    rows = len(grid)
    cols = len(grid[0])
    q = deque()

    land = 0 
    water = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                q.append((r,c))
                land += 1
            else:
                water += 1
    if land == 0 and water == 0:
        return -1        

    # directions
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    dist = -1
    while q:
        size = len(q)
        for _ in range(size):

            r,c = q.popleft()
            
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                    if grid[nr][nc] == 0:
                        q.append((nr,nc))
                        #marked visited water
                        grid[nr][nc] = 1
            
        # if q:
        dist += 1
    return dist

print(water_from_land([[1,0,1],[0,0,0],[1,0,1]]))