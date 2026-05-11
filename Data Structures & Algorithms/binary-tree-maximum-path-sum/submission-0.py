# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = root.val
        def dfs(node) -> int:
            if not node:
                return 0
            nonlocal ans
            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left + right + node.val, left + node.val, right + node.val, node.val)
            return max(left, right, 0) + node.val
        dfs(root)
        return ans