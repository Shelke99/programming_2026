# class medianFinder()
import heapq
data = []
# medianFinder()
def add_num(num):
    heapq.heappush(data,num)
   

def findMedian():
    arr = sorted(data)
    sz = len(arr)
    if sz % 2 == 0:
        return arr[sz // 2]
    else:
        return  arr[sz // 2 - 1] + arr[sz // 2] // 2.0
   

# add_num(10)
add_num(20)
# add_num(90)
# add_num(40)
# add_num(70)
print(findMedian())

