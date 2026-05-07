# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative DFS
        if not root:
            return 0
        ans = 1
        stack = [[root, 1]]

        while stack:
            curr, lvl = stack.pop()
            if curr:
                ans = max(ans, lvl)
                stack.append([curr.left, lvl + 1])
                stack.append([curr.right, lvl + 1])
        return ans
