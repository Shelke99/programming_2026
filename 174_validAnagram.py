class Solution:
    def validAnagram(self,s,t):
        if len(s) != len(t):
            return False
        
        st = {}
        ts = {}

        for i in s:
            st[i] = st.get(i, 0) + 1
        for j in t:
            ts[j] = ts.get(j, 0) + 1
        for i in st:
            if i not in ts and st[i] != ts[i]:
                return False 
        return True
sol = Solution()
print(sol.validAnagram('anagram', 'nagaram'))
        