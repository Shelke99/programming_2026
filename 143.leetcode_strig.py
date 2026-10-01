def leetcode(strs):

    if not strs:
        return ""


    result = ""


    for c in range(0, len(strs[0])):
        flag = True
        ch = strs[0][c]

        
        for r in range(1,len(strs)):
            if c >= len(strs[r]) or strs[r][c] != ch:
                flag = False
                break
        if flag == True:
            result += ch
        else:
            return result
    return result
print(leetcode(["flower", "flow", "flight"]))  # Output: "fl"

