class Solution:
    def reversString(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            s[l],s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s
s = Solution()
print(s.reversString('h','e'))


