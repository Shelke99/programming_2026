from collections import deque
def removeAdjDuplicate(s):
    stack = deque()
    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
print(removeAdjDuplicate("abbaca"))