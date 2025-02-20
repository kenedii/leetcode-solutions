# Beats 100% Runtime, Beats 90.99% memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a,b = [], [] # a=p, b=q
        def recurse_preorder(root, pq, lr=''):
            if root is None:
                if pq == 'p':
                    if lr == 'left':
                        a.append("le") # left is empty
                    else:
                        a.append("re") # right is empty
                else:
                    if lr == 'left':
                        b.append("le") # left is empty
                    else:
                        b.append("re") # right is empty
                return
            if pq=='p':
                a.append(root.val)
                recurse_preorder(root.left, 'p', 'left')
                recurse_preorder(root.right, 'p', 'right')
            else:
                b.append(root.val)
                recurse_preorder(root.left, 'q', 'left')
                recurse_preorder(root.right, 'q', 'right')
        recurse_preorder(p, 'p')
        recurse_preorder(q, 'q')
        return a == b
            
