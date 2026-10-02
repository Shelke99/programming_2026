def findDisapperedNum(nums):
    dic = {}
    ans = []
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    for i in range(1,len(nums)+1):
        if i not in dic:
            ans.append(i)
    return ans
print(findDisapperedNum([1,3,4,6,7,8]))