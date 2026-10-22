# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = [root]
        l = 1

        s = []

        while q:
            x = []
            l = len(q)
            for i in range(l):
                v = q.pop(0)
                x.append(v.val)
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            s.append(x)
    
        return s
            