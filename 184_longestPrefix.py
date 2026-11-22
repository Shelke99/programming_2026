class FindPrefix:
    def longestPrefix(self,strs):
        if not len(strs):
            return " "
        result = ""
        for i in range(0,len(strs[0])):
            c = strs[0][i]
            flag = True
            for r in range(1, len(strs)):
                if i >= len(strs[r]) or strs[r][i] != c:
                    flag = False

            if flag == True:
                result += c 
                # return result
            else:
                return result
        return result
f = FindPrefix()
print(f.longestPrefix(['ram', 'rama','rani']))