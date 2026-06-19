import heapq
def k_closest(points, k):
    heap = []
    for i, (x,y) in enumerate(points):
        dist = x * x + y * y
        heapq.heappush(heap,(dist,i))
    ans = []
    for _ in range(k):
        dist, idx = heapq.heappop(heap)
        ans.append(points[idx])
    return ans
print(k_closest([[1,3],[-2,2]],1))