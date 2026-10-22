# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = []
        l = 0

        if not root:
            return []
        
        q.append(root)
        l = 1

        s = []

        while q:
            new_l = 0
            x = []
            for i in range(l):
                v = q.pop(0)
                # print(l, v.val)
                x.append(v.val)
                if v.left:
                    q.append(v.left)
                    new_l += 1
                if v.right:
                    q.append(v.right)
                    new_l += 1
            s.append(x)
            l = new_l
    
        return s
            