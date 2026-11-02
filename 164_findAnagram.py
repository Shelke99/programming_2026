class Solution:
    def findAnagram(self,s,k):
        if len(s) != len(k):
            return False
        c = {}
        r = {}
        for i in s:
            c[i] = c.get(i,0) + 1
        for j in k:
            r[j] = r.get(j,0) + 1
        for b in c:
            if b not in r or c[b] != r[b]:
                return False
        return True
sol = Solution()
print(sol.findAnagram('anagram','nagaram'))
