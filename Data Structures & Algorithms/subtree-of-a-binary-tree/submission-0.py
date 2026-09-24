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

        return self.isEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isEqual(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        
        if a and b:
            if a.val == b.val:
                return True and self.isEqual(a.left, b.left) and self.isEqual(a.right, b.right)
            else:
                return False
        elif not a and not b:
            return True
        return False