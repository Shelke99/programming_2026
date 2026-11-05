class Solution:
    def validAnagram(self,s,t):
        if len(s) != len(t):
            return False
        p = {}
        q = {}
        for i in s:
            p[i] = p.get(i, 0) + 1
        for j in t:
            q[j] = q.get(j, 0) + 1
        for ch in p:
            if ch not in q or p[ch] != q[ch]:
                return False 
        return True
sol = Solution()
print(sol.validAnagram('anagram', 'nagaram'))