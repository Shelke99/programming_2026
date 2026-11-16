class Solution:
    def lengthOfLastWord(self, s):
        sz = 0
        i = len(s) - 1
        while (i >= 0 and s[i] == " "):
            i -= 1
        while (i >= 0 and s[i] != " "):
            sz += 1
            i -= 1
        return sz
sol = Solution()
print(sol.lengthOfLastWord('I go Far'))
