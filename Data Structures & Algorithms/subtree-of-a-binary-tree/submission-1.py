# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return (
            self.isEqual(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isEqual(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True

        if a and b and a.val == b.val:
            return self.isEqual(a.left, b.left) and self.isEqual(a.right, b.right)

        return False