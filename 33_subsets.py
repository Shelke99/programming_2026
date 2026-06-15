# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
def subset(num):
    ans = []
    cur = []
    backTrack(0,cur,num,ans)
    return ans
def backTrack(indx,cur,num,ans):
    # base case
    if(indx == len(num)):
        ans.append(cur[:])
        return ans
    # include current element
    cur.append(num[indx])
    
    backTrack(indx + 1,cur,num,ans)
    # backTrack
    cur.pop()
    # exclude current element
    backTrack(indx + 1,cur,num,ans)
print(subset([1,2,3]))



