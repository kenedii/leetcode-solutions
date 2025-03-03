# Beats 96.95% Runtime O(N∗Log(N)) Complexity
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        final = []
        for node in lists:
            cur = node
            while cur is not None:
                final.append(cur.val)
                cur = cur.next
        if len(final) == 0:
            return
        final.sort()
        cur=ListNode()
        root = cur
        for i in range(0,len(final)):
            cur.val = final[i]
            cur.next = ListNode() if i != len(final)-1 else None
            cur = cur.next
        return root
