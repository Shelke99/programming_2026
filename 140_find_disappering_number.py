def disappeared_num(nums):
    dic = {}
    ans = []
    for i in nums:
        flag = 0
        dic[i] = dic.get(i, 0) + 1


    # for j in range(1, len(dic) + 1):
    #     if j == dic:
    #         flag = 1
    #         break

    # if flag == 0:
    #     ans.append(j)
    # return ans
    for j in range(1, len(nums) + 1):
        if j not in dic:
            ans.append(j)
    return ans


    # print(dic)
print(disappeared_num([4,3,2,7,8,2,3,1]))