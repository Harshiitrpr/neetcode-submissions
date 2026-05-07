# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        if not root:
            return True
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            if abs(left - right) > 1:
                ans = False
            return 1 + max(left, right)
        dfs(root)
        return ans
        