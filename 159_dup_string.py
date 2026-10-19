from collections import deque
def dupRemove(s):
    stk = deque()
    for ch in s:
        if stk and ch == stk[-1]:
            stk.pop()
        else:
            stk.append(ch)
    return "".join(stk)
print(dupRemove("abbaca"))
