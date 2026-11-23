from collections import deque

class Duplicate:
    def removeDup(self,strs):
        st = deque()
        for i in strs:
            if st  and st[-1] == i:
                st.pop()
            else:
                st.append(i)
        return "".join(st)
d = Duplicate()
print(d.removeDup('aaca'))
