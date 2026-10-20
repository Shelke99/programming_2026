# def isSameTree(p, q):
#     if p is None and q is None:
#         return True

#     if p is None or q is None:
#         return False

#     if p != q:
#         return False

#     return (isSameTree(p.le, q.left) and
#             isSameTree(p.right, q.right))
# print(isSameTree([1,2,3],[1,2,3]))
def isSameTree(p, q):
    if p == q:
        return True
    return False

print(isSameTree([1, 2, 3], [1, 2, 3]))  # True
print(isSameTree([1, 2, 3], [1, 2, 4]))  # False