from collections import deque
# class Solution:
def findOrder(numCourses, prerequisites):
    #build adjacency list and in_degree array
    adj_list = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses

    for dest, src in prerequisites:
        adj_list[src].append(dest)
        in_degree[dest] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    ans = []

    while queue:
        course = queue.popleft()
        ans.append(course)
        for neighbor in adj_list[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return ans if len(ans) == numCourses else []
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
