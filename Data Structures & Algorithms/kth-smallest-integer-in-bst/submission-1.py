# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traversal(node):
            if node:
                yield from traversal(node.left)
                yield node.val
                yield from traversal(node.right)

        
        for i, val in enumerate(traversal(root), 1):
            if i == k:
                return val
