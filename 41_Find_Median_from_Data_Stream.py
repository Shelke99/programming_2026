# class medianFinder()
import heapq
data = []
# medianFinder()
def add_num(num):
    heapq.heappush(data,num)
   
ans = 0
def findMedian():
    arr = sorted(data)
    sz = len(data)
    if sz % 2 == 0:
        return data[sz // 2]
    else:
        return  arr[sz // 2 - 1] + arr[sz // 2] / 2
   

add_num(10)
add_num(20)
add_num(30)
add_num(40)

print(findMedian())

