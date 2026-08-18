def intervals(I):
    sz = len(I)
    if sz == 1:
        return I 
    ans = []
    # I_value = sorted(I)
    I = sorted(I, key=lambda x: x[0])
    print(I)
    start = I[0][0]
    end =  I[0][1]
    for i in range(1, sz):
        if I[i][0] <= end:
            end = I[i][1]
        else:
            ans.append({start,end})
            start = I[i][0]
            end = I[i][1]
    ans.append({start, end})
    return ans
print(intervals([[1,3],[2,6],[8,10],[15,18]]))

