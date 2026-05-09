# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        idx = 0
        ans = 0
        def dfs(node):
            nonlocal idx,ans
            if node.left:
                dfs(node.left)
            idx += 1
            if idx == k:
                ans = node.val
                idx += 1
                return
            elif idx >= k:
                return
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans
        