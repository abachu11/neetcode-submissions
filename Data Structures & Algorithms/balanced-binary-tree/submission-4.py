# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode]) -> (int, bool):
            if node is None:
                return (0, True)  # Base case: height is 0 and it's balanced

            left_depth, left_balanced = dfs(node.left)
            right_depth, right_balanced = dfs(node.right)

            # The tree is balanced if both subtrees are balanced and the height difference is <= 1
            balanced = left_balanced and right_balanced and abs(left_depth - right_depth) <= 1

            # Return the height of the current subtree and if it's balanced
            return (max(left_depth, right_depth) + 1, balanced)

        return dfs(root)[1]

             