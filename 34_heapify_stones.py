import heapq
def heapify_stones(stones):
    sz = len(stones)
    # convert to max heap
    stones = [-stone for stone in stones]

    heapq.heapify(stones)

    if sz == 1:
        return stones[0]

    while len(stones) > 1:
        # largest sstone
        h = -heapq.heappop(stones)
        
        # second largest stone
        l = -heapq.heappop(stones)
        
        if h != l:
            heapq.heappush(stones, -(h - l))
    # return heapq.size() == 0 ? 0 heapq.top():
    if len(stones) == 0:
        return 0
    else:
        return -stones[0]
print(heapify_stones([1,2,3,4,5,6,7,8,9]))

