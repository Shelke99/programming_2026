# leetcode problem 57 insert intervals
def interval(Itr,nI):
    I = list(Itr)
    I.append(nI)
    I.sort(key = lambda x:x[0])
             #1
    start = I[0][0]
           #3
    end = I[0][1] 
    ans = []

    for i in range(1, len(I)):
                #2 < 3
        if I[i][0] <= end:
            end = max(end,I[i][1])
        else:
            ans.append([start, end])
            start,end = I[i]
    ans.append([start,end])
    return ans
print(interval([[1,3],[6,8]],[2,5]))

