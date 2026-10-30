# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isNodeValid(node: Optional[TreeNode], lowerBound, upperBound) -> Bool:
            
            if not node:
                return True

            if node.val < upperBound and node.val > lowerBound:
                return isNodeValid(node.left, lowerBound, node.val) and isNodeValid(node.right, node.val, upperBound)
            
            return False

        return isNodeValid(root, float('-inf'), float('inf'))
    