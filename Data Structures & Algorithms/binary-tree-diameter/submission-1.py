# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia_diff = 0
        def dfs(root):
            nonlocal dia_diff

            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            dia_diff = max(dia_diff,right_depth + left_depth)
            return 1+max(left_depth,right_depth)

        dfs(root)
        return dia_diff