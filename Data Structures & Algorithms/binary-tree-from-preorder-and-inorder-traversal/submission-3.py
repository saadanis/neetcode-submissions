# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {inorder[i] : i for i in range(len(inorder))}

        def builder(pre_start, in_start, in_end) -> Optional[TreeNode]:

            if in_end <= in_start:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(val=root_val)

            root_in_inorder = inorder_map[root_val]

            root.left = builder(
                pre_start+1,
                in_start,
                root_in_inorder)

            root.right = builder(
                pre_start + root_in_inorder - in_start + 1,
                root_in_inorder+1,
                in_end)

            return root

        return builder(0, 0, len(preorder))