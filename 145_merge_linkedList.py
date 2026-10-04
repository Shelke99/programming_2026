
# def mergeLinkedList(list1, list2):
#     dummy = ListNode(0)
#     current = dummy 
#     while list1 and list2:
#         if list1.val <= list2.val:
#             current.next = list1
#             list1 = list1.next
#         else:
#             current.next = list2
#             list2 = list2.next

#         current = current.next
#     if list1:
#         current.next = list1
#     else:
#         current.next = list2    
#     return dummy.next
# print(mergeLinkedList([1,2,3],[3,4,5]))
# -------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedList(list1, list2):
    dummy = ListNode(0)
    current = dummy 
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    else:
        current.next = list2    
    return dummy.next

# Create the lists manually line-by-line to save space
l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(3, ListNode(4, ListNode(5)))

# Merge and pull the values to print
res = mergeLinkedList(l1, l2)
print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val, res.next.next.next.next.next.val)
