# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        def dfs(node, k):
            nonlocal ans
            if node.val >= k:
                ans += 1
            if node.left:
                dfs(node.left, max(k, node.val))
            if node.right:
                dfs(node.right, max(k, node.val))
        dfs(root, root.val)
        return ans
                
        