from collections import deque
class Solution:
    def removeAllAdjcentDuplicateInString(self,s):
        st = deque()
        for i in s:
            if st and i == st[-1]:
                st.pop()
            else:
                st.append(i)
        return ''.join(st)
sol = Solution()
print(sol.removeAllAdjcentDuplicateInString('abbaca'))
