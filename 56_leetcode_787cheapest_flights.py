# class Solution:
def Cheapest_Flights(n, flights, src, dst, k):
    INF = float('inf')
    dist = [INF] * n
    dist[src] = 0
    
    for _ in range(k + 1):
        temp = dist.copy()
        
        for u,v, price in flights:
            if dist[u] == INF:
                continue
            if dist[u] + price < temp[v]:
                temp[v] = dist[u] + price
        dist = temp
    return -1 if dist[dst] == INF else dist[dst]
print(Cheapest_Flights(5,[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1))
    