# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_d, right_d = 0,0
        if root.left:
            left_d = self.maxDepth(root.left)
        
        if root.right:
            right_d = self.maxDepth(root.right)

        return (max(left_d,right_d)+1)
        