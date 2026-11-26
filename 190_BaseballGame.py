class Baseball:
    def baseBallGame(self, s):
        result = []
        for i in s:
                
            if i == '+':
                result.append(result[-1] + result[-2])
            elif i == 'D':
                result.append(result[-1] * 2)
            elif i == 'C':
                result.pop()
            else:
                result.append(int(i))
        ans = 0 
        for i in result:
            ans += i
        return ans
B = Baseball()
print(B.baseBallGame(["5","2","C","D","+"]))

